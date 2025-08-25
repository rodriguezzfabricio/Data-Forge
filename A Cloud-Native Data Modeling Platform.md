# DataForge: A Cloud-Native Data Modeling Platform - Technical Blueprint and Implementation Plan

## Section 1: Strategic Foundation and Cost Optimization

This section establishes the project's financial and resource management strategy, a critical prerequisite for a student-led initiative. The approach outlined here provides a strategic guide to navigating the cloud ecosystem with minimal to zero cost, ensuring that learning objectives are met without incurring unexpected financial burdens.

### 1.1 A Student's Guide to Cloud Economics: Maximizing Free Resources

The foundation of this project's feasibility rests on the strategic use of free-tier services and student-specific benefits. A well-planned approach to resource activation and utilization is paramount.

#### The GitHub Student Developer Pack as Your Launchpad

The GitHub Student Developer Pack is the central hub for acquiring the necessary professional-grade tools at no cost. Its value extends beyond simple software access to providing a robust, cloud-based development environment that standardizes the workflow for both the developer and the AI coding agent.

- **GitHub Pro Features:** The pack grants a GitHub Pro account, which includes essential features like unlimited private repositories, 20 GB of Codespaces storage, and a significant monthly allowance of 3,000 Actions minutes.^1^
- **GitHub Codespaces:** This is a key strategic asset. By providing a powerful, cloud-based development environment accessible from any internet-connected device, Codespaces eliminates local machine configuration issues ("it works on my machine") and ensures a consistent, customizable platform for development.^1^ For this project, it is recommended to use Codespaces as the primary IDE to create a stable and replicable environment for the AI agent to operate within.
- **GitHub Copilot Pro:** The pack includes free access to GitHub Copilot Pro, the AI-powered coding companion. This tool will be instrumental in accelerating development, but its effectiveness is directly tied to the quality and specificity of the instructions it receives, a core challenge this report aims to solve.^1^
- **Partner Offers:** The pack includes numerous partner offers. Of particular note is the DigitalOcean credit, which typically provides around $200.^2^ This should be viewed as a valuable secondary cloud environment for experimentation or as a backup, allowing for isolated tests without consuming primary AWS credits.

#### Navigating the New AWS Free Tier (Post-July 15, 2025)

For new AWS accounts created after July 15, 2025, the Free Tier model has shifted from a 12-month, usage-based system to a 6-month, credit-based program.^3^ This change fundamentally alters the project timeline, transforming it from a year-long marathon into a focused, 6-month development sprint.

- **Free Plan vs. Paid Plan:** Upon signup, new users are presented with two options: a "Free Plan" and a "Paid Plan".^4^ It is strongly recommended to select the
  **Free Plan** . This plan ensures that no charges will be incurred until the user explicitly upgrades to a paid plan. The account and its resources will be closed after 6 months or when credits are exhausted, with a 90-day grace period to upgrade and recover data.^6^ This acts as a critical financial safety net, preventing accidental overages that are common for students learning cloud services.^8^
- **Credit Structure:** The new model provides an initial $100 in AWS credits upon sign-up. An additional $100 can be earned by completing specific learning-oriented activities, such as launching an EC2 instance or setting up an AWS Budget.^4^ This totals up to $200 in credits to be used within the 6-month "Free Plan" period. This budget must be carefully managed to cover the costs of services that are not part of the "Always Free" tier, such as running an Amazon RDS instance.
- **Strategic Timeline:** The 6-month expiration of the Free Plan dictates the project's pace. The most credit-intensive phases of development and learning, particularly those involving the continuous operation of an RDS database instance, must be planned and executed within this window. After the initial 6 months, the project architecture should be capable of running in a "maintenance mode" that relies exclusively on AWS's "Always Free" services, such as AWS Lambda and DynamoDB.

#### Leveraging AWS Educate

As a parallel resource, AWS Educate offers a separate, no-credit-card-required learning environment.^10^ This platform provides free, self-paced online training and hands-on labs for core services like Amazon S3, Amazon EC2, Amazon VPC, and Amazon RDS. Utilizing AWS Educate for foundational learning allows the developer to gain practical experience and familiarity with the AWS console and service configurations without consuming the main account's limited 6-month credits. This preserves the primary credit budget for the actual development and deployment of the DataForge project.

### 1.2 Implementing Proactive Cost Governance

Passive reliance on free tiers is insufficient; active cost management is a mandatory skill for any cloud developer. Setting up automated alerts is the first and most crucial step to be taken immediately after creating an AWS account.

#### Mandatory First Step: AWS Budgets and Billing Alarms

AWS provides two primary tools for cost control: AWS Budgets and Amazon CloudWatch Alarms. Both should be configured to create a robust safety net.

A step-by-step guide to setting up a "zero-spend" budget and a low-threshold billing alarm:

1. **Enable Billing Alerts:** Before creating any alarms, you must first enable billing data access.
   - Sign in to the AWS Management Console. In the top-right corner, click on your account name and select "Billing & Cost Management Dashboard".^11^
   - In the left navigation pane, select "Billing preferences".^12^
   - Check the box for "Receive Billing Alerts" and save the preferences. This allows billing metric data to be published to CloudWatch.^11^ It may take around 15-30 minutes for the data to become available.^12^
2. **Create an AWS Budget:** This tool monitors your spending against a set amount and can alert you based on actual or forecasted costs.
   - In the Billing & Cost Management console, navigate to "Budgets" in the left pane.^13^
   - Click "Create a budget" and select the "Use a template (simplified)" option.^4^
   - Choose the **"Zero spend budget"** template. This template is specifically designed to notify you when your AWS spending exceeds $0.01.^13^
   - Configure the notification to send an email alert to your address when the actual spend exceeds 100% of the budget (i.e., exceeds $0.01). This provides an immediate warning the moment any cost is incurred.
3. **Create a CloudWatch Billing Alarm:** This provides a secondary layer of protection by monitoring the total estimated charges for your account.
   - Navigate to the CloudWatch service in the AWS Management Console. **Crucially, you must switch your region to "US East (N. Virginia) `us-east-1`"** , as this is where global billing data is stored.^11^
   - In the left navigation pane, under "Alarms", select "Billing".^11^
   - Click "Create alarm".
   - The metric will be `EstimatedCharges` under the "Billing" namespace, with the currency in USD. Select this metric.^12^
   - Under "Conditions", set the threshold type to "Static" and define the condition as "Greater/Equal" to a low monetary value, for example, **$5.00** .^11^ This means the alarm will trigger if your estimated monthly charges exceed $5.
   - Click "Next". On the "Configure actions" page, create a new Amazon SNS (Simple Notification Service) topic and enter your email address as the endpoint. You will receive a confirmation email that you must click to enable notifications.^11^
   - Give the alarm a descriptive name (e.g., `TotalCharges-Exceeds-5USD`) and complete the creation process.

By implementing both a zero-spend budget and a low-threshold billing alarm, you create a dual-alert system that effectively prevents unexpected charges and enforces cost-conscious development practices from day one.

### 1.3 Table: Student Cloud Resource and Cost Strategy

The following table synthesizes the available resources and cost-avoidance tactics into a coherent strategy, providing a quick-reference guide for the project's lifecycle.

| Resource                       | Benefit / Limit                                                                                    | Activation Strategy                                                                                                 | Cost-Avoidance Tactic                                                                                                                                                          |
| ------------------------------ | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --- | --- |
| **GitHub Codespaces**          | 180 core hours/month, 20 GB storage^1^                                                             | Activate immediately upon starting the project.                                                                     | Configure Codespaces to auto-shutdown after a short period of inactivity (e.g., 30 minutes) to conserve hours.                                                                 |
| **GitHub Copilot Pro**         | Free for verified students^1^                                                                      | Activate immediately. Use for code completion and boilerplate generation.                                           | Use highly specific prompts based on the implementation plan to maximize effectiveness and reduce rework.                                                                      |
| **AWS Free Tier Credits**      | Up to $200 in credits, expiring 6 months after signup (for accounts created post-July 15, 2025)^3^ | Create AWS account only when ready to begin active development to maximize the 6-month window.                      | Implement a "zero-spend" AWS Budget and a $5 CloudWatch billing alarm immediately upon account creation. Shut down credit-consuming resources like RDS when not in active use. |     |     |
| **AWS "Always Free" Services** | Perpetual free usage within monthly limits (e.g., 1M Lambda requests, 25 GB DynamoDB storage)^15^  | Design the application's long-term state to rely on these services after the initial 6-month credit period expires. | Architect the backend API to be stateless and fit within Lambda's execution limits. Use DynamoDB for session data and other simple key-value storage needs.                    |
| **DigitalOcean Credits**       | $200 credit, valid for one year for new users^2^                                                   | Activate as a secondary environment for isolated experiments or for hosting non-critical services.                  | Use this credit for tasks that might be expensive or unpredictable on AWS, preserving the core AWS credits for the main project deployment.                                    |

## Section 2: Architectural Blueprint: A Domain-Driven Approach

This section translates the DataForge project concept into a formal software architecture, grounded in the principles of Domain-Driven Design (DDD). This architectural choice is not merely academic; it is a pragmatic solution to ensure the application is modular, maintainable, and, critically, structured in a way that an AI coding agent can effectively interpret and implement. The complexity of the system is managed by breaking it down into logical, business-focused components.

### 2.1 Deconstructing the Domain: The University Course Registration System

The foundation of DDD is a deep understanding of the business domain. For DataForge, the chosen domain is a university course registration system. This domain is complex enough to be meaningful, with intricate rules and relationships that provide a rich ground for applying DDD principles.

#### Establishing a Ubiquitous Language

A core tenet of DDD is the development of a _Ubiquitous Language_ —a shared, unambiguous vocabulary used by all team members (in this case, the developer and the AI agent) and reflected directly in the code.^17^ This eliminates confusion and ensures that the software model accurately represents the business domain.

For this project, the Ubiquitous Language will include the following core terms:

- **`Student`** : An individual enrolled at the university.
- **`Course`** : A specific class offered by a department, such as "CS101 - Introduction to Programming".
- **`Department`** : An academic unit that offers courses, like "Computer Science".
- **`Prerequisite`** : A course that must be completed before a student can enroll in another course.
- **`Enrollment`** : The act and record of a `Student` registering for a `Course` in a specific `Semester`.
- **`CourseCatalog`** : The complete collection of all `Courses` offered by the university.
- **`Semester`** : A specific academic term (e.g., "Fall 2025").

These terms will be used for class names, variable names, and database table names, creating a direct and intuitive link between the business problem and the software solution.

#### Defining Bounded Contexts

A complex domain is best understood by breaking it down into smaller, more manageable sub-domains known as _Bounded Contexts_ . Each Bounded Context has its own distinct model and language, and is decoupled from others, allowing for independent development and clear separation of concerns.^17^ This partitioning is essential for providing the AI agent with focused, isolated tasks.

The system will be divided into the following Bounded Contexts:

- **Catalog Management Context** : This context is responsible for all aspects of defining and managing the university's academic offerings. Its core concerns are the creation, updating, and querying of `Courses`, `Departments`, and their associated `Prerequisites`.
- **Student Enrollment Context** : This context focuses on the student's journey through the registration process. It manages the `Student` profile and their `Enrollments` in specific `Courses`. The business logic for verifying prerequisites and checking course capacity resides here.
- **Identity and Access Context** : This context is a supporting domain responsible for handling user authentication and authorization. It manages user credentials and ensures that only authenticated and authorized users can perform specific actions (e.g., only a registered `Student` can enroll in a `Course`).

### 2.2 Modeling a Core Business Process: The `Enrollment` Aggregate

In DDD, an _Aggregate_ is a cluster of associated objects that are treated as a single unit for the purpose of data changes. The entry point to the aggregate is an entity known as the _Aggregate Root_ . All external references are restricted to the Aggregate Root, which is responsible for ensuring the consistency and validity of the entire aggregate through every transaction.^19^ This pattern is crucial for encapsulating complex business rules.

#### Aggregate Root as a Consistency Boundary

For the course registration system, the `Enrollment` process is a prime candidate for an Aggregate. An `Enrollment` is not just a simple link between a student and a course; it is a transactional boundary governed by business rules (invariants). For an enrollment to be valid, the `Student` must have met all `Prerequisites`, and the `Course` must have available capacity. The `Enrollment` Aggregate Root will enforce these invariants. By channeling all modifications through the Aggregate Root, the system guarantees that it is impossible to create an invalid enrollment state.^19^

#### Practical Java Example of the `Enrollment` Aggregate

The following Java code provides a concrete example of an `Enrollment` Aggregate Root. This is a "rich" domain model, where business logic is encapsulated within the entity itself, avoiding the anemic domain model anti-pattern where entities are merely data holders.^17^

**Java**

```
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import java.util.Set;

@Entity
@Table(name = "enrollments")
public class Enrollment {

    @Id
    private String enrollmentId;
    private String studentId;
    private String courseId;
    private EnrollmentStatus status;

    // Private constructor for JPA
    protected Enrollment() {}

    // Factory method to create a new enrollment attempt
    public static Enrollment attempt(String studentId, Course course) {
        // Initial state is PENDING
        return new Enrollment(studentId, course.getCourseId(), EnrollmentStatus.PENDING);
    }

    private Enrollment(String studentId, String courseId, EnrollmentStatus status) {
        this.enrollmentId = java.util.UUID.randomUUID().toString();
        this.studentId = studentId;
        this.courseId = courseId;
        this.status = status;
    }

    /**
     * Business logic to confirm the enrollment.
     * This method enforces the invariants of the aggregate.
     * @param completedPrerequisites The set of courses the student has already completed.
     * @param course The course object to enroll in, containing prerequisite and capacity info.
     */
    public void confirm(Set<Course> completedPrerequisites, Course course) {
        if (this.status!= EnrollmentStatus.PENDING) {
            throw new IllegalStateException("Enrollment can only be confirmed from PENDING state.");
        }

        // Invariant 1: Check prerequisites
        if (!course.arePrerequisitesMet(completedPrerequisites)) {
            this.status = EnrollmentStatus.FAILED_PREREQUISITES;
            throw new PrerequisiteNotMetException("Student has not met all prerequisites for this course.");
        }

        // Invariant 2: Check course capacity
        if (!course.hasCapacity()) {
            this.status = EnrollmentStatus.FAILED_CAPACITY;
            throw new CourseCapacityExceededException("Course has no available seats.");
        }

        // If all invariants are satisfied, the state transition is valid.
        this.status = EnrollmentStatus.ENROLLED;
        course.decrementCapacity(); // The aggregate can trigger side effects on other entities within its boundary.
    }

    public void drop() {
        if (this.status!= EnrollmentStatus.ENROLLED) {
            throw new IllegalStateException("Cannot drop a course that is not in ENROLLED state.");
        }
        this.status = EnrollmentStatus.DROPPED;
    }

    // Getters...
}

enum EnrollmentStatus {
    PENDING,
    ENROLLED,
    DROPPED,
    FAILED_PREREQUISITES,
    FAILED_CAPACITY
}
```

### 2.3 Structuring the Spring Boot Application for DDD

The project's package structure must reflect the DDD layers to enforce separation of concerns and maintain the integrity of the domain model. A common anti-pattern in simple Spring applications is to organize packages by technical type (e.g., `controllers`, `services`, `repositories`), which leads to high coupling and a "big ball of mud" architecture over time.^22^ Instead, a structure organized by domain feature or Bounded Context is superior.

The dependency rule is paramount: the `domain` layer must not have any dependencies on other layers. The `application` and `infrastructure` layers depend on the `domain` layer, but never the other way around.^17^ This ensures the core business logic is pure and independent of any specific technology (like Spring MVC or PostgreSQL), making it highly portable and testable.

#### Recommended Package Structure

```
com.dataforge
└───core
    ├───application
    │   ├───dto                     // Data Transfer Objects for API communication
    │   │   └───enrollment
    │   └───service                 // Application services that orchestrate use cases
    │       └───EnrollmentService.java
    │
    ├───domain
    │   ├───catalog                 // Catalog Management Bounded Context
    │   │   ├───model               // Entities, Value Objects
    │   │   │   └───Course.java
    │   │   └───repository          // Repository interfaces
    │   │       └───CourseRepository.java
    │   └───enrollment              // Student Enrollment Bounded Context
    │       ├───model               // Aggregates, Entities
    │       │   └───Enrollment.java
    │       └───repository
    │           └───EnrollmentRepository.java
    │
    └───infrastructure
        ├───config                  // Spring configuration (Security, CORS, etc.)
        │   └───SecurityConfig.java
        ├───persistence             // Data persistence implementations
        │   └───repository
        │       └───JpaEnrollmentRepository.java // Implements EnrollmentRepository
        └───web
            └───controller          // REST controllers
                └───EnrollmentController.java
```

This structure creates clear, logical boundaries that are easy for both a human developer and an AI agent to navigate. It isolates the core business rules in the `domain` package, separates the use case orchestration in the `application` package, and pushes all external-facing concerns (web servers, database connections) to the `infrastructure` package. This organization directly supports the goal of providing clear, context-specific instructions to the AI coding agent, as each task can be precisely located within a specific package and layer.

## Section 3: Backend Implementation Plan for the AI Coding Agent (`BACKEND_PLAN.md`)

This document serves as a detailed, step-by-step implementation guide for the DataForge backend. It is structured into epics and tasks, formatted in Markdown to be directly consumable by a developer or an AI coding agent like GitHub Copilot. Each task is designed to be a discrete, actionable unit of work.

# DataForge Backend Implementation Plan

This plan outlines the development tasks for the Java/Spring Boot backend. Follow each task sequentially to build the application.

## Epic 1: Core Domain Model and Persistence Layer

**Objective:** Establish the foundational business objects and their connection to the PostgreSQL database using Domain-Driven Design principles and JPA.

- [ ] **Task 1.1: Define Core JPA Entities**
  - Create Java classes for `Student`, `Course`, `Department`, and `Prerequisite` in the `com.dataforge.core.domain` package structure.
  - Annotate each class with `@Entity` and `@Table` from `jakarta.persistence`.
  - Define fields for each entity, including primary keys (`@Id`, `@GeneratedValue`) and relationships (`@ManyToOne`, `@OneToMany`, `@ManyToMany`). For example, a `Course` has a `@ManyToOne` relationship with a `Department`.^23^
- [ ] **Task 1.2: Implement the `Enrollment` Aggregate Root**
  - Create the `Enrollment.java` class in the `com.dataforge.core.domain.enrollment.model` package.
  - Implement the class as a rich domain object, including fields for `studentId`, `courseId`, and `status`.
  - Encapsulate business logic within methods like `confirm(..)` and `drop()`, which enforce invariants such as prerequisite checks and capacity limits.^19^
- [ ] **Task 1.3: Create Spring Data JPA Repository Interfaces**
  - In the `com.dataforge.core.domain.<context>.repository` packages, create Java interfaces for each Aggregate Root.
  - Example: `public interface EnrollmentRepository extends JpaRepository<Enrollment, String> {}`.
  - These interfaces define the contract for data persistence but contain no implementation details, adhering to the DDD principle of keeping the domain layer clean.^17^
- [ ] **Task 1.4: Configure Database Connection and Schema Management**
  - In src/main/resources/application.properties, configure the connection to your PostgreSQL database:properties
    spring.datasource.url=jdbc:postgresql://localhost:5432/dataforge_db
    spring.datasource.username=your_username
    spring.datasource.password=your_password
    spring.jpa.database-platform=org.hibernate.dialect.PostgreSQLDialect
  - Set the schema generation property: `spring.jpa.hibernate.ddl-auto=update`. **Note:** This is for initial local development ONLY to quickly create tables. This will be changed to `validate` or `none` later, as the application's core purpose is to manage schema changes via user input, not automatically from entities.^25^
- [ ] **Task 1.5: Integrate Flyway for Database Migrations**
  - Add the Flyway dependency to your `pom.xml`: `flyway-core`.
  - Create a directory `src/main/resources/db/migration`.
  - Flyway will be used programmatically in a later epic to apply the SQL DDL generated by the frontend. For now, its presence establishes the migration framework. This is a critical architectural decision: the backend does not manage its own schema; it executes schemas defined by the user.^28^

## Epic 2: RESTful API for Course and Enrollment Management

**Objective:** Expose the core domain functionality through a secure and well-defined RESTful API.

- [ ] **Task 2.1: Implement `CourseController`**
  - Create a Spring `@RestController` in the `com.dataforge.core.infrastructure.web.controller` package.
  - Implement endpoints for `GET /api/courses`, `GET /api/courses/{id}`, `POST /api/courses`, etc., to manage the `CourseCatalog`.
- [ ] **Task 2.2: Implement `EnrollmentController`**
  - Create another `@RestController` for enrollments.
  - Implement `POST /api/enrollments` to handle a new enrollment request. This endpoint will accept a DTO containing `studentId` and `courseId`.
  - Implement `GET /api/students/{studentId}/schedule` to retrieve a student's enrolled courses.
- [ ] **Task 2.3: Implement Application Services**
  - In the `com.dataforge.core.application.service` package, create services like `EnrollmentService`.
  - These services will orchestrate the business logic. For example, `EnrollmentService.enrollStudent()` will fetch the `Student` and `Course` entities, invoke the `enrollment.confirm()` method on the domain aggregate, and save the result using the repository.
  - Use `@Transactional` on service methods to ensure atomicity.^17^
- [ ] **Task 2.4: Configure Global CORS**
  - Create a `@Configuration` class that implements `WebMvcConfigurer`.
  - Override the `addCorsMappings` method to define a global CORS policy. Allow requests from the React frontend's development server (e.g., `http://localhost:3000`).
  - Specify allowed methods (`GET`, `POST`, `PUT`, `DELETE`), headers (`Authorization`, `Content-Type`), and credentials (`allowCredentials(true)`).^31^

## Epic 3: Schema Generation and Validation Service

**Objective:** Build the core functionality of the DataForge platform: generating and previewing database schema changes based on user input from the frontend.

- [ ] **Task 3.1: Create Schema Management Endpoint**
  - In a new `SchemaController`, create a `POST /api/schema/preview` endpoint.
  - This endpoint will accept a JSON object representing the desired database schema (tables, columns, relationships) designed by the user in the React frontend.
- [ ] **Task 3.2: Implement Schema Comparison Logic**
  - Create a `SchemaComparisonService`.
  - This service will need to get the current schema of the connected PostgreSQL database.
  - It will then compare the current schema with the target schema received from the frontend. Libraries like `jOOQ` provide powerful DDL interpretation and diffing capabilities that can be used here.^33^ SchemaCrawler is another alternative.^34^
- [ ] **Task 3.3: Implement "Dry Run" DDL Generation**
  - Based on the comparison from the previous task, generate the necessary SQL DDL statements (`CREATE TABLE`, `ALTER TABLE ADD COLUMN`, etc.) to migrate the current schema to the target schema.
  - **Crucially, do not execute these statements.** Return the generated SQL script as a string in the API response. This is the "real-time DDL preview" feature. This concept is similar to the "dry run" feature in migration tools like Flyway Teams or Liquibase.^35^
- [ ] **Task 3.4: Create Schema Deployment Endpoint**
  - Create a `POST /api/schema/deploy` endpoint.
  - This endpoint will receive the same target schema JSON.
  - The service will generate the DDL script as before, but this time it will save it as a new Flyway migration file (e.g., `V{timestamp}__user_generated_schema.sql`) and then programmatically invoke Flyway to apply the migration to the database.^30^

## Epic 4: Stateless Security & Session Management

**Objective:** Secure the API using modern, stateless authentication with JWTs and manage user sessions efficiently using a cloud-native database.

- [ ] **Task 4.1: Integrate Spring Security 6**
  - Ensure `spring-boot-starter-security` is in the `pom.xml`.
  - Create a `SecurityConfig` class annotated with `@Configuration` and `@EnableWebSecurity`.
  - Define a `SecurityFilterChain` bean. In this bean, disable CSRF, configure `http` rules to permit access to `/api/auth/**` and require authentication for all other `/api/**` paths. Set the session management policy to `STATELESS`.^38^
- [ ] **Task 4.2: Implement JWT-Based Authentication**
  - Add the `jjwt` library dependencies to `pom.xml`.
  - Create a `JwtService` class to handle token generation (upon successful login) and validation (parsing claims, checking expiration). The JWT secret key should be externalized in `application.properties`.^39^
  - Create a `JwtAuthenticationFilter` that extends `OncePerRequestFilter`. This filter will execute for each request, extract the JWT from the `Authorization: Bearer <token>` header, validate it using `JwtService`, and if valid, set the authenticated user in the `SecurityContextHolder`.^39^
  - Add this custom filter to the `SecurityFilterChain` before the `UsernamePasswordAuthenticationFilter`.
- [ ] **Task 4.3: Implement Cloud-Native Session Management**
  - **Option A (Recommended for Cost): DynamoDB**
    - Add the community-supported `spring-session-dynamodb` dependency.^42^
    - Configure `application.properties` with your AWS region and credentials.
    - Annotate a configuration class with `@EnableDynamoDBHttpSession`.
    - **Note:** This library is experimental. Proceed with caution and be prepared for potential issues.^42^ This approach leverages DynamoDB's generous "Always Free" tier, making it ideal for a long-term, low-cost student project.^43^
  - **Option B (Recommended for Robustness & Learning): Redis with ElastiCache**
    - Add the official `spring-session-data-redis` and `spring-boot-starter-data-redis` dependencies.
    - Annotate a configuration class with `@EnableRedisHttpSession`.^45^
    - Configure the `application.properties` to connect to your AWS ElastiCache for Redis endpoint.^46^
    - This approach uses an officially supported Spring module and provides exposure to another key AWS service, aligning with learning goals. It will consume AWS credits while the Free Tier is active.^47^

```

## Section 4: Frontend Implementation Plan for the AI Coding Agent (`FRONTEND_PLAN.md`)

This document provides a detailed, step-by-step implementation guide for the DataForge frontend. It is structured into epics and tasks, formatted in Markdown to be directly consumable by a developer or an AI coding agent. The primary focus is on building the visual schema designer.

# DataForge Frontend Implementation Plan

This plan outlines the development tasks for the React frontend application. The core feature is a visual, drag-and-drop schema designer for relational databases.

## Epic 5: Building the Visual Schema Designer with React Flow

**Objective:** Create an interactive canvas where users can visually design database schemas by creating tables and defining relationships.

-   [ ] **Task 5.1: Project Setup**
    -   Initialize a new React project using Vite for a fast development experience: `npm create vite@latest dataforge-ui -- --template react-ts`.
    -   Install the necessary libraries: `@xyflow/react` for the diagramming canvas and `dnd-kit` for foundational drag-and-drop utilities.[48, 49, 50]

-   [ ] **Task 5.2: Create the Main Canvas Component**
    -   Create a main component (e.g., `SchemaCanvas.tsx`).
    -   Wrap the component's content with the `<ReactFlowProvider>` and render the `<ReactFlow />` component inside it. This component will serve as the main interactive area.[51]

-   [ ] **Task 5.3: Develop a Custom "Table" Node**
    -   Create a new React component, `TableNode.tsx`. This will be a custom node representing a database table.
    -   The component should render a container with a header for the table name (e.g., an `<input type="text">`) and a body area for listing columns.
    -   Register this component in your `SchemaCanvas.tsx` using the `nodeTypes` prop: `const nodeTypes = { table: TableNode };`.[52]

-   [ ] **Task 5.4: Implement Dynamic Columns within the Table Node**
    -   Inside `TableNode.tsx`, use React state (`useState`) to manage an array of columns. Each column object should have properties like `id`, `name`, and `dataType`.
    -   Render a row for each column in the state. Each row should contain an input for the column name and a dropdown (`<select>`) for the data type (e.g., `VARCHAR(255)`, `INTEGER`, `BOOLEAN`, `TIMESTAMP`).
    -   Add a button within the node (e.g., "+ Add Column") that, when clicked, adds a new column object to the component's state, triggering a re-render with a new empty row.

-   [ ] **Task 5.5: Implement Custom Connection Handles**
    -   For each column row rendered in `TableNode.tsx`, add a `<Handle />` component from `@xyflow/react`.
    -   Each handle represents a connection point for a relationship (an edge). Assign a unique `id` to each handle, likely corresponding to the column's name or ID.
    -   Configure handles on both the left (`type="target"`) and right (`type="source"`) sides of the column row to allow for incoming (foreign key) and outgoing (primary key) connections.[52, 53]

## Epic 6: State Management and Real-time Validation

**Objective:** Implement robust state management for the entire schema graph and enforce data integrity through real-time validation of user inputs and relationships.

-   [ ] **Task 6.1: Integrate Zustand for Global State Management**
    -   Install Zustand: `npm install zustand`.
    -   Create a `store.ts` file to define the global state store. This store will manage the arrays of `nodes` and `edges` for the entire React Flow canvas.
    -   The React Flow documentation recommends Zustand for complex applications where state needs to be accessed and modified from within custom nodes, which is exactly our use case.[54, 55, 56]

-   [ ] **Task 6.2: Implement Connection Validation**
    -   In `SchemaCanvas.tsx`, define an `isValidConnection` callback function.
    -   Pass this function to the `<ReactFlow />` component's `isValidConnection` prop.
    -   Inside the function, implement logic to enforce relational database rules. For example, check the data types of the source and target columns to ensure they are compatible for a foreign key relationship. You can prevent connections that violate logical constraints (e.g., connecting a column to itself).[57, 58]

-   [ ] **Task 6.3: Implement In-Node Form Validation**
    -   Install React Hook Form: `npm install react-hook-form`.
    -   Inside the `TableNode.tsx` component, wrap the input fields for the table name and column names with `useForm` from React Hook Form.
    -   Apply validation rules, such as `required` and `pattern` (e.g., to prevent special characters or SQL keywords in table/column names).
    -   Display clear, inline error messages next to the input fields when validation fails. This provides immediate feedback to the user.[59, 60, 61]

## Epic 7: DDL Preview and Backend Integration

**Objective:** Translate the visual schema into a SQL DDL script in real-time and connect the frontend to the backend API to save and deploy the schema.

-   [ ] **Task 7.1: Create the DDL Preview Component**
    -   Create a new component, `DdlPreview.tsx`. This component will display the generated SQL script inside a read-only text area or a code viewer component.

-   [ ] **Task 7.2: Convert React Flow State to JSON Schema**
    -   Create a utility function that subscribes to changes in the Zustand store.
    -   This function's responsibility is to traverse the `nodes` (tables) and `edges` (relationships) arrays from the store and transform this graph data into a structured JSON object that conforms to a defined JSON Schema format. This JSON representation will be the standardized format for communicating the schema to the backend.

-   [ ] **Task 7.3: Generate DDL from JSON Schema in Real-Time**
    -   Install a client-side library capable of this transformation, such as `json-schema-to-sql`.[62]
    -   In the `DdlPreview.tsx` component, use the utility function from the previous task to get the latest JSON schema from the Zustand store.
    -   Pass this JSON schema to the `json-schema-to-sql` library's generation function.
    -   The output will be a SQL DDL string. Render this string within the component. This process will re-run whenever the store updates, creating the "real-time" preview effect.

-   [ ] **Task 7.4: Implement API Client with React Query**
    -   Install React Query: `npm install @tanstack/react-query`.
    -   Wrap the application in a `QueryClientProvider`.
    -   Create custom hooks (e.g., `useCourseCatalog`, `useDeploySchema`) that use React Query's `useQuery` and `useMutation` hooks.
    -   React Query will automatically handle API request states, including loading indicators, error messages, caching, and retries, simplifying the logic for interacting with the backend.[63, 64, 65]

-   [ ] **Task 7.5: Implement Schema Deployment**
    -   Add a "Deploy Schema" button to the UI.
    -   When clicked, this button will trigger the `useDeploySchema` mutation hook from React Query.
    -   The hook will send the final, validated JSON schema from the Zustand store to the backend's `/api/schema/deploy` endpoint (defined in Backend Epic 3).

## Section 5: Cloud Infrastructure and Deployment Pipeline

This section provides the blueprint for deploying the full-stack DataForge application to AWS. The architecture is designed to be cost-effective, align with the student's learning objectives by exposing them to core cloud concepts, and be fully automated through a CI/CD pipeline.

### 5.1 Deployment Architecture on AWS: A Pragmatic Approach

The selection of AWS services is guided by a balance between ease of management, learning value, and cost-effectiveness within the constraints of the AWS Free Tier and student credits.

#### Compute - AWS Elastic Beanstalk

For the Spring Boot backend, **AWS Elastic Beanstalk** is the recommended deployment target. While a serverless approach using AWS Lambda is a viable alternative for long-term cost savings, Elastic Beanstalk offers a superior learning experience for a student developer. It automates the provisioning of a traditional application environment, yet it keeps the underlying resources—such as EC2 instances, Auto Scaling Groups, and Elastic Load Balancers—visible and configurable through its console.[66] This transparency is invaluable for understanding how the components of a scalable web application fit together.

Elastic Beanstalk itself is a free service; costs are incurred only for the AWS resources it provisions to run the application, such as the EC2 instance.[67] These costs will be covered by the initial $200 in Free Tier credits during the first 6 months of the project. A migration to AWS Lambda could be a future enhancement, but starting with Elastic Beanstalk provides a more foundational understanding of cloud infrastructure.[68, 69, 70]

#### Relational Database - Amazon RDS for PostgreSQL

The primary transactional database for the course registration system will be hosted on **Amazon RDS for PostgreSQL**. RDS is a managed database service that automates time-consuming administration tasks like patching, backups, and scaling.[71] To remain within a cost structure that is well-covered by the new credit-based Free Tier, the deployment should be configured as follows:
*   **Instance Class:** `db.t3.micro` or `db.t4g.micro`. These are small, burstable instances suitable for development and low-traffic applications.[71]
*   **Storage:** 20 GB of General Purpose SSD (`gp2`) storage.[71]
*   **Deployment:** Single-AZ (Availability Zone) deployment to minimize cost. Multi-AZ is for high-availability production workloads and would consume credits at double the rate.

A sample AWS CloudFormation template can be used to automate the provisioning of this RDS instance, introducing the developer to Infrastructure as Code (IaC) principles.[72, 73]

#### NoSQL/Session Store - Amazon DynamoDB

For managing user sessions, **Amazon DynamoDB** is the ideal choice due to its inclusion in the "Always Free" tier. This makes it the most cost-effective, long-term solution that will continue to operate at no cost even after the initial 6-month credits are exhausted. The Always Free tier for DynamoDB includes:
*   25 GB of storage.
*   25 Write Capacity Units (WCU).
*   25 Read Capacity Units (RCU).

This is more than sufficient to handle the session management needs of a student project, capable of handling up to 200 million requests per month.[43, 44] A CloudFormation template will be used to define and create the necessary DynamoDB table for storing session data, ensuring its configuration is version-controlled and repeatable.[74]

### 5.2 Table: AWS Service Selection and Free Tier Analysis

This table provides a consolidated view of the chosen AWS services, their role in the project, and a clear strategy for managing their usage within the free tier.

| Service | Role in Project | Free Tier Limit (New Credit Model) | Monitoring & Alerting Strategy |
| :--- | :--- | :--- | :--- |
| **AWS Elastic Beanstalk** | Application Orchestration & Deployment | The service itself is free; underlying resources consume credits.[67] | Monitor the health of the environment. Set up notifications for deployment failures. |
| **Amazon EC2** | Compute for Backend (provisioned by Beanstalk) | Covered by the initial $200 in credits. Use a `t2.micro` or `t3.micro` instance.[75, 76] | Monitor `CPUUtilization` and `CPUCreditBalance` in CloudWatch to ensure the instance is not being throttled. |
| **Amazon RDS (PostgreSQL)** | Relational Data Store | Covered by the initial $200 in credits. Use a `db.t3.micro` instance with 20 GB `gp2` storage.[71] | Set CloudWatch alarms on `FreeableMemory` (to detect memory pressure) and `CPUUtilization`. |
| **Amazon DynamoDB** | Session Store | 25 GB storage, 25 WCU, 25 RCU (Always Free).[43, 44] | Monitor `ConsumedReadCapacityUnits` and `ConsumedWriteCapacityUnits`. Set alarms if usage approaches the free tier limits. |
| **GitHub Actions** | CI/CD Pipeline | 2,000 minutes/month (Free plan), 3,000 minutes/month (Pro plan via Student Pack).[1] | Monitor build minute usage in the GitHub account settings. Optimize workflows to minimize build times. |

### 5.3 Automated CI/CD with GitHub Actions

A fully automated Continuous Integration and Continuous Deployment (CI/CD) pipeline is a hallmark of modern software development and a key learning objective. GitHub Actions will be used to automate the entire process from code commit to deployment on AWS.

#### Workflow Configuration (`.github/workflows/deploy.yml`)

A production-ready workflow file will be created in the project repository. This workflow will trigger on every push to the `main` branch.

#### Workflow Steps:

1.  **Checkout Code:** The workflow begins by checking out the latest version of the source code using the standard `actions/checkout@v3` action.
2.  **Set up JDK:** The environment is prepared for a Java build using `actions/setup-java@v3`, specifying a version compatible with Spring Boot 3 (e.g., Java 17).
3.  **Configure AWS Credentials:** To securely interact with AWS, the workflow will use the `aws-actions/configure-aws-credentials` action. The recommended authentication method is OpenID Connect (OIDC), which allows the workflow to assume an IAM role in AWS without needing to store long-lived `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` as GitHub Secrets. This is a modern security best practice that avoids secret sprawl.[77, 78]
4.  **Backend Build & Integration Test:** The backend is built and tested using the Maven command `mvn clean verify`. A critical part of this step is the execution of integration tests using **Testcontainers**. Before deployment, Testcontainers will programmatically spin up temporary Docker containers for PostgreSQL and Redis/DynamoDB on the GitHub Actions runner. The integration tests will run against these real, ephemeral database instances, providing high confidence that the application interacts correctly with its dependencies. This practice prevents bugs that often arise from discrepancies between local development environments and the CI environment.[79, 80, 81, 82]
5.  **Frontend Build:** The workflow will then switch to the frontend directory, install dependencies with `npm install`, and create a production build with `npm run build`.
6.  **Package and Deploy to Elastic Beanstalk:** The final step involves packaging the backend JAR file and the static frontend build assets into a deployment bundle. This bundle is then deployed to the pre-configured AWS Elastic Beanstalk environment using a dedicated GitHub Action for Elastic Beanstalk deployment, triggering a new version rollout.[83, 84]

## Section 6: Conclusion and Future Enhancements

This project, when completed, will represent a significant achievement for a student developer. It goes beyond a typical CRUD application, incorporating advanced architectural patterns, a complex user interface, and a professional-grade cloud deployment strategy.

### 6.1 Project Retrospective and Learning Outcomes

Successfully building DataForge will provide tangible evidence of proficiency in a wide range of highly marketable skills. The completed project will serve as a powerful portfolio piece, demonstrating:
*   **Full-Stack Development:** Expertise in building and integrating a Java/Spring Boot backend with a modern React frontend.
*   **Cloud-Native Architecture:** Practical experience in designing, deploying, and managing applications on AWS using core services like Elastic Beanstalk, RDS, and DynamoDB.
*   **Advanced Software Design:** A deep, practical understanding of Domain-Driven Design principles, including Bounded Contexts and Aggregates, for managing complexity in enterprise applications.
*   **DevOps and Automation:** The ability to construct a complete, automated CI/CD pipeline using GitHub Actions, including best practices like OIDC for security and Testcontainers for reliable integration testing.
*   **Cloud Financial Management:** A demonstrated understanding of cloud economics, including navigating free tiers, implementing cost-control measures, and making architectural decisions based on financial constraints.

### 6.2 Pathways for Extension

The architecture of DataForge is designed to be extensible. Upon completion of the core features, several advanced pathways are available for further learning and enhancement.

*   **NoSQL Schema Visualization:** The most direct extension is to enhance the React Flow designer to support NoSQL data modeling. This would involve creating new custom nodes to represent DynamoDB's key-value structure (partition keys, sort keys) and document models, providing a visual way to design and generate schemas for both relational and NoSQL databases.
*   **Event-Driven Architecture:** To further embrace modern design patterns, the `Enrollment` process could be refactored to be event-driven. Instead of a synchronous process, the `Enrollment` aggregate could publish an `EnrollmentConfirmed` domain event. This event could be sent to an Amazon SNS topic, which then triggers an AWS Lambda function to perform asynchronous tasks, such as sending a confirmation email to the student. This would decouple the system's components and introduce the developer to event-driven patterns.
*   **Serverless Migration:** As a cost-optimization and advanced learning exercise, the backend could be migrated from Elastic Beanstalk to a fully serverless architecture using AWS Lambda and Amazon API Gateway. This would involve refactoring the Spring Boot application to run within the Lambda execution environment using the AWS Serverless Java Container library.[70, 85] Deployment would be managed using the AWS Serverless Application Model (SAM), providing experience with another powerful IaC tool.[86, 87] This architecture would be extremely cost-effective, primarily leveraging the "Always Free" tier for long-term hosting after the initial credits expire.
*   **Infrastructure as Code (IaC) Deep Dive:** While this plan introduces IaC with CloudFormation templates for specific resources, a comprehensive next step would be to codify the *entire* infrastructure—VPC, security groups, IAM roles, Elastic Beanstalk environment, etc.—using CloudFormation or Terraform. This would achieve a fully automated, repeatable, and version-controlled infrastructure setup, a critical skill in modern cloud operations.
```
