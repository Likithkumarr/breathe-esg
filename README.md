# Breathe ESG Data Ingestion Platform

## Project Overview

This project is a full-stack ESG data ingestion and review platform.

The system allows:
- CSV upload
- Data normalization
- Suspicious record detection
- Analyst review workflow
- Approve/reject actions
- Audit logging

---

## Tech Stack

### Frontend
- React
- Vite
- Axios

### Backend
- Django
- Django REST Framework

### Database
- PostgreSQL

### Deployment
- Render (Backend)
- Vercel (Frontend)

---

## Features

- Upload CSV files
- Normalize ESG records
- Detect suspicious values
- Review dashboard
- Approve/reject workflow
- Audit trail logging
- Production deployment

---

## API Endpoints

### Upload CSV
POST /api/upload/

### Review Records
GET /api/review/

### Approve/Reject
POST /api/review/<id>/

---

## Deployment Links

Frontend:
https://breathe-esg-black.vercel.app

Backend:
https://breathe-esg-87pg.onrender.com

GitHub:
https://github.com/Likithkumarr/breathe-esg

---

## Author

Likith Kumar