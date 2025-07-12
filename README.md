# AutoApply

AutoApply is a full-stack web application for automating job applications. It features a Django/PostgreSQL backend and a React/TypeScript frontend styled with Tailwind CSS.

## Project Structure

- `backend/` — Django REST API, authentication, and business logic
- `frontend/` — React SPA for user interaction
- `docs/` — Documentation

## Quick Start

### Backend

See [backend/README.md](backend/README.md)

### Frontend

See [frontend/README.md](frontend/README.md)

### Documentation

See [docs/](docs/)

---

## License

MIT

# Backend — AutoApply

This is the backend for AutoApply, built with Django and Django REST Framework.

## Features

- JWT authentication (SimpleJWT + Djoser)
- Custom user model with profile (skills, resume, etc.)
- PostgreSQL database
- CORS enabled for frontend integration

## Setup

1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

2. **Configure database:**
   Edit `autoapply/settings.py` with your PostgreSQL credentials.

3. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

4. **Create superuser:**
   ```sh
   python manage.py createsuperuser
   ```

5. **Run server:**
   ```sh
   python manage.py runserver
   ```

## Apps

- `users` — Custom user and profile
- `jobs` — (To be implemented)
- `automation` — (To be implemented)

## API

- Auth endpoints via Djoser at `/auth/`
- User and profile endpoints (see docs)

## Environment

- Python 3.10+
- PostgreSQL

## License

MIT

# Frontend — AutoApply

This is the frontend for AutoApply, built with React, TypeScript, and Tailwind CSS.

## Features

- React SPA (bootstrapped with Create React App)
- TypeScript for type safety
- Tailwind CSS for styling
- API integration with Django backend

## Setup

1. **Install dependencies:**
   ```sh
   npm install
   ```

2. **Start development server:**
   ```sh
   npm start
   ```
   The app will be available at [http://localhost:3000](http://localhost:3000).

## Scripts

- `npm start` — Start dev server
- `npm run build` — Build for production
- `npm test` — Run tests

## Configuration

- Tailwind config: `tailwind.config.js`
- PostCSS config: `craco.config.js`
- TypeScript config: `tsconfig.json`

## License

MIT