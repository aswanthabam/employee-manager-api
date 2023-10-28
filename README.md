# Employee Manager API

Designing and developing an efficient employee management system is crucial for businesses to streamline their human resources processes. The challenge is to create a web application with REST API endpoints that allow CRUD (Create, Read, Update, Delete) operations on employee and department data. Additionally, the system should include functionality to assign employees to departments and promote eligible employees to manager positions based on experience criteria.

## API End points

- `/api/auth/register/`
- `/api/auth/token/`
- `/api/organization/`
- `/api/organization/create/`
- `/api/organization/update/`
- `/api/organization/delete/`
- `/api/organization/<org_id>/departments/`
- `/api/organization/<org_id>/departments/create/`
- `/api/organization/<org_id>/departments/update/`
- `/api/organization/<org_id>/departments/delete/`
- `/api/organization/<org_id>/departments/<dep_id>/employee/`
- `/api/organization/<org_id>/departments/<dep_id>/employee/create/`
- `/api/organization/<org_id>/departments/<dep_id>/employee/update/`
- `/api/organization/<org_id>/departments/<dep_id>/employee/delete/`
