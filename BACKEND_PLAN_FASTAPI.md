# DataForge Backend Implementation Plan (FastAPI)

This plan outlines the development tasks for the Python/FastAPI backend. Follow each task sequentially to build the application.

## Epic 1: Core Domain Model and Persistence Layer

**Objective:** Establish the foundational business objects and their connection to the PostgreSQL database using Domain-Driven Design principles and SQLAlchemy.

- [ ] **Task 1.1: Project Setup and Dependency Management**
  - Initialize a new Python project with a virtual environment.
  - Install FastAPI, Uvicorn, SQLAlchemy, Pydantic, and other necessary libraries.
  - Create a `requirements.txt` file to manage dependencies.

- [ ] **Task 1.2: Define Core SQLAlchemy Models**
  - Create Python classes for `Student`, `Course`, `Department`, and `Prerequisite` in a `dataforge/core/domain` directory structure.
  - Use SQLAlchemy's Declarative Base to define these classes as ORM models.
  - Define fields for each model, including primary keys and relationships (`relationship`, `ForeignKey`).

- [ ] **Task 1.3: Implement the `Enrollment` Aggregate Root**
  - Create the `Enrollment.py` class in the `dataforge/core/domain/enrollment/model` directory.
  - Implement the class as a rich domain object, including fields for `student_id`, `course_id`, and `status`.
  - Encapsulate business logic within methods like `confirm()` and `drop()`, which enforce invariants such as prerequisite checks and capacity limits.

- [ ] **Task 1.4: Create Repository Interfaces and Implementations**
  - In a `dataforge/core/domain/<context>/repository` directory, create repository interfaces (abstract base classes).
  - Create SQLAlchemy implementations of these repositories in the `dataforge/core/infrastructure/persistence/repository` directory.

- [ ] **Task 1.5: Configure Database Connection and Schema Management**
  - In a `config.py` file or using environment variables, configure the connection to your PostgreSQL database.
  - Use Alembic for database migrations. Initialize Alembic in the project. This will be used to manage schema changes.

## Epic 2: RESTful API for Course and Enrollment Management

**Objective:** Expose the core domain functionality through a secure and well-defined RESTful API.

- [ ] **Task 2.1: Implement `CourseController`**
  - Create a FastAPI router in the `dataforge/core/infrastructure/web/controller` directory.
  - Implement endpoints for `GET /api/courses`, `GET /api/courses/{id}`, `POST /api/courses`, etc., to manage the `CourseCatalog`.

- [ ] **Task 2.2: Implement `EnrollmentController`**
  - Create another FastAPI router for enrollments.
  - Implement `POST /api/enrollments` to handle a new enrollment request. This endpoint will accept a Pydantic model containing `student_id` and `course_id`.
  - Implement `GET /api/students/{student_id}/schedule` to retrieve a student's enrolled courses.

- [ ] **Task 2.3: Implement Application Services**
  - In the `dataforge/core/application/service` directory, create services like `EnrollmentService`.
  - These services will orchestrate the business logic. For example, `EnrollmentService.enroll_student()` will fetch the `Student` and `Course` entities, invoke the `enrollment.confirm()` method on the domain aggregate, and save the result using the repository.

- [ ] **Task 2.4: Configure Global CORS**
  - In the main FastAPI application file, add CORS middleware to allow requests from the React frontend's development server.

## Epic 3: Schema Generation and Validation Service

**Objective:** Build the core functionality of the DataForge platform: generating and previewing database schema changes based on user input from the frontend.

- [ ] **Task 3.1: Create Schema Management Endpoint**
  - In a new `SchemaController`, create a `POST /api/schema/preview` endpoint.
  - This endpoint will accept a JSON object representing the desired database schema from the React frontend.

- [ ] **Task 3.2: Implement Schema Comparison Logic**
  - Create a `SchemaComparisonService`.
  - This service will get the current schema of the connected PostgreSQL database.
  - It will then compare the current schema with the target schema received from the frontend.

- [ ] **Task 3.3: Implement "Dry Run" DDL Generation**
  - Based on the comparison from the previous task, generate the necessary SQL DDL statements.
  - Return the generated SQL script as a string in the API response.

- [ ] **Task 3.4: Create Schema Deployment Endpoint**
  - Create a `POST /api/schema/deploy` endpoint.
  - This endpoint will receive the same target schema JSON.
  - The service will generate the DDL script and save it as a new Alembic migration file, then apply the migration.

## Epic 4: Stateless Security & Session Management

**Objective:** Secure the API using modern, stateless authentication with JWTs.

- [ ] **Task 4.1: Integrate JWT-Based Authentication**
  - Add a library like `python-jose` for JWT creation and validation.
  - Create a `JwtService` to handle token generation and validation.
  - Create a dependency function that can be used with FastAPI's dependency injection system to protect endpoints.

- [ ] **Task 4.2: Implement User Authentication Flow**
  - Create endpoints for user registration and login.
  - Upon successful login, generate and return a JWT.
