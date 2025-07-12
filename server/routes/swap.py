from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.swap import Swap, SwapStatus
from models.user import User
from schemas.swap import SwapCreate, SwapOut
from utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/swap", tags=["Swap"])

@router.post("/send", response_model=SwapOut)
def send_swap(request: SwapCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    if user.id == request.receiver_id:
        raise HTTPException(status_code=400, detail="Cannot swap with yourself")
    swap = Swap(requester_id=user.id, receiver_id=request.receiver_id, message=request.message)
    db.add(swap)
    db.commit()
    db.refresh(swap)
    return swap

@router.get("/pending", response_model=list[SwapOut])
def view_pending_swaps(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return db.query(Swap).filter(
        (Swap.requester_id == user.id) | (Swap.receiver_id == user.id),
        Swap.status == SwapStatus.pending
    ).all()

@router.post("/accept/{swap_id}")
def accept_swap(swap_id: int, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    swap = db.query(Swap).filter(Swap.id == swap_id).first()
    if swap.receiver_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    swap.status = SwapStatus.accepted
    db.commit()
    return {"message": "Swap accepted"}

@router.post("/reject/{swap_id}")
def reject_swap(swap_id: int, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    swap = db.query(Swap).filter(Swap.id == swap_id).first()
    if swap.receiver_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    swap.status = SwapStatus.rejected
    db.commit()
    return {"message": "Swap rejected"}

@router.delete("/delete/{swap_id}")
def delete_swap(swap_id: int, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    swap = db.query(Swap).filter(Swap.id == swap_id).first()
    if swap.requester_id != user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    db.delete(swap)
    db.commit()
    return {"message": "Swap deleted"}