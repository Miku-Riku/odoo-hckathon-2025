from fastapi import FastAPI
from routes import auth, user, swap, admin, feedback, message  # ✅ routes, not models!

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(user.router, prefix="/user")
app.include_router(swap.router, prefix="/swap")
app.include_router(admin.router, prefix="/admin")
app.include_router(feedback.router, prefix="/feedback")
app.include_router(message.router, prefix="/messages")  # ✅ optional for all-platform messages

@app.get("/")
def root():
    return {"message": "Skill Swap API is running"}
