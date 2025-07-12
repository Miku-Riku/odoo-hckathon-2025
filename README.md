# odoo-hackathon-2025 (failed to finish frontend and run into bugs, but databse design and backend is finished)
📚 Skill Swap Platform
A mini platform that allows users to offer and request skills in exchange. Users can list their skills, search others, request swaps, and provide feedback. Admins can moderate the platform.

🗂️ Project Structure
bash
Copy
Edit
skill-swap/
├── backend/                # FastAPI server
└── frontend/               # Next.js (React) frontend with Tailwind CSS
⚙️ Backend (FastAPI)
🔧 Tech Stack
FastAPI

PostgreSQL

SQLAlchemy

JWT Authentication

Passlib (bcrypt)

Pydantic

Uvicorn

▶️ How to Run Backend
1. Setup a virtual environment:
bash
Copy
Edit
cd backend
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Mac/Linux
2. Install dependencies:
bash
Copy
Edit
pip install -r requirements.txt
If you don’t have requirements.txt, generate it using:

bash
Copy
Edit
pip freeze > requirements.txt
3. Set Environment Variables
Create a .env file in the backend folder:

ini
Copy
Edit
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
DATABASE_URL=postgresql://<user>:<password>@localhost/<your-db-name>
4. Run the server:
bash
Copy
Edit
uvicorn main:app --reload
Then go to http://127.0.0.1:8000/docs to access the Swagger UI.

📦 DB Migration
Use alembic or run:

bash
Copy
Edit
from database import Base, engine
Base.metadata.create_all(bind=engine)
🧪 Backend Features
✅ JWT Authentication
✅ User Registration/Login
✅ List/Update Profile
✅ Skills Offered/Wanted
✅ Skill Swap Requests
✅ Accept/Reject/Delete Requests
✅ Ratings and Feedback
✅ Admin Actions (ban user, broadcast, reject skills)

🧑‍🎨 Frontend (Next.js + Tailwind)
🔧 Tech Stack
Next.js 14+

React

TypeScript

Tailwind CSS

Axios

▶️ How to Run Frontend
1. Navigate to frontend:
bash
Copy
Edit
cd frontend
2. Install dependencies:
bash
Copy
Edit
npm install
3. Start the dev server:
bash
Copy
Edit
npm run dev
Visit: http://localhost:3000

🔐 Environment Variables (Frontend)
Create .env.local in the frontend/ directory:

ini
Copy
Edit
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
📁 Frontend Folder Structure
bash
Copy
Edit
frontend/
├── src/
│   ├── app/
│   │   ├── page.tsx             # Home page
│   │   ├── login/page.tsx       # Login page
│   │   ├── register/page.tsx    # Registration page
│   │   ├── profile/page.tsx     # User profile page
│   │   ├── swap/page.tsx        # Swap listings
│   │   ├── admin/page.tsx       # Admin panel (if logged in as admin)
│   ├── components/              # Reusable components
│   ├── lib/                     # Helper functions (e.g., Axios client)
│   ├── types/                   # Type definitions
├── tailwind.config.js
├── postcss.config.js
└── .env.local
🧠 Tips
Use Swagger (/docs) to test API routes.

Make sure the backend is running before using the frontend.

Customize Tailwind styles in tailwind.config.js.

📮 Contribution
PRs are welcome. Please create issues for bugs or features.

🧼 To Do
 Add Pagination to Browse/Search

 Notification System

 Deploy to Vercel (frontend) and Render (backend)