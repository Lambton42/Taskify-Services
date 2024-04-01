# Taskify-Services
An Agile Scrum Task board Backend Services

API detailes:
1. API Endpoints: where FastAPI application instance is created and configured.
   i.issues.py: Create, read, update, and delete for issues. Also search and filter issues by criteria
   ii. projects.py: Create, read, update, and delete for projects. This file manages project roles and permissionss.
   iii. Users.py: this file manages the user registration, authentication, and profile management.
   iv. workflows.py: this file defines and manages the workflow states for issues.
3. Dependency
   i. database.py: this file establishes database connections and sessions
   ii. permission.py: this file manages permission checks and role-based access control
   iii. security.py: this file handles anthentication, token generation and verification.
5. Schemas: in this section we define the Pydantic models for input validation and serialization of output for the Endpoints.