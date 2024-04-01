Admin Features:
    Manage Project:
        Projects Database:
            localhost:8080/API/v1/project/id/1
            [Post, Put, Get, Delete]
        Create Project:
            POST localhost:8080/API/v1/projects/id
        Search Project:
            GET localhost:8080/API/v1/projects?search=id
        Delete Project:
            Delete localhost:8080/API/v1/projects/id
        List Project Table:
            GET localhost:8080/API/v1/projects
    User Management:
        Users Database:
            localhost:8080/API/v1/User/id/1
            [Post, Put, Get, Delete]
            localhost:8080/API/v1/Users
        Invite Member: (send user invitation by email)
            POST localhost:8080/API/v1/projects/id/Users/id
        List User Table:
            GET localhost:8080/API/v1/projects/id/Users
        User status:
            GET localhost:8080/API/v1/Users/id/status
        Update User Last active:
            GET localhost:8080/API/v1/Users/id/lastActive
            PATCH localhost:8080/API/v1/Users/id
        User Detailed Name Card:
            GET localhost:8080/API/v1/Users/id/fullname
            GET localhost:8080/API/v1/Users/id/emailaddress
            GET localhost:8080/API/v1/Users/id/publicname
    Task Board Management:
        Tasks Database:
            localhost:8080/API/v1/task/id/1
            [Post, Put, Get, Delete]
            localhost:8080/API/v1/tasks
        Column Search Box:
	        GET localhost:8080/API/v1/tasks?search={keywords}
        Task Filter:
            GET localhost:8080/API/v1/tasks?User=id
        Assignees:
            GET localhost:8080/API/v1/tasks/id/assignee
        Task number:
            GET localhost:8080/API/v1/columns/id/tasks/count
        Three dot actions rename:
            PUT localhost:8080/API/v1/tasks/id/taskname
        Three dot actions delete:
            DELETE localhost:8080/API/v1/tasks/id
        Task card actions copy link:
            GET localhost:8080/API/v1/tasks/id/link
        Task card move position:
            PUT localhost:8080/API/v1/tasks/id/position
        Task card actions delete:
            DELETE localhost:8080/API/v1/tasks/id
        Task title
            GET localhost:8080/API/v1/tasks/id/title
            PUT localhost:8080/API/v1/tasks/id/title
        Task Assignee:
            GET localhost:8080/API/v1/tasks/id/assignee
            PUT localhost:8080/API/v1/tasks/id/assignee
        Task Project initials:
            GET localhost:8080/API/v1/tasks/id/initial
            PUT localhost:8080/API/v1/tasks/id/initial
        No.task:
            GET localhost:8080/API/v1/tasks/id/tasknumber
        Create new task:
            POST localhost:8080/API/v1/tasks/id
    Task Card Details:
        Task Card Status:
            Assignee: 
                GET localhost:8080/API/v1/tasks/id/assignee
                PUT localhost:8080/API/v1/tasks/id/assignee
            Reporter: 
                GET localhost:8080/API/v1/tasks/id/reporter
                PUT localhost:8080/API/v1/tasks/id/reporter
            Priority: 
                GET localhost:8080/API/v1/tasks/id/priority
                PUT localhost:8080/API/v1/tasks/id/priority
            Status: 
                GET localhost:8080/API/v1/tasks/id/status
                PUT localhost:8080/API/v1/tasks/id/status
            Due Date: 
                GET localhost:8080/API/v1/tasks/id/duedate
                PUT localhost:8080/API/v1/tasks/id/duedate
            Category:
                GET localhost:8080/API/v1/tasks/id/category
                PUT localhost:8080/API/v1/tasks/id/category
            TimE Tracking: 
                GET localhost:8080/API/v1/tasks/id/timetracking
                PUT localhost:8080/API/v1/tasks/id/timetracking
    Task Content:
        Title: GET localhost:8080/API/v1/tasks/id/title
        Description:GET/PUT localhost:8080/API/v1/tasks/id/description
        Activity:
            Comments: 
                GET localhost:8080/API/v1/tasks/id/comments
                POST localhost:8080/API/v1/tasks/id/comments
                DELETE localhost:8080/API/v1/tasks/id/comments	
            History: 
                GET localhost:8080/API/v1/tasks/id/history
            Work Log: 
                GET/POST localhost:8080/API/v1/tasks/id/worklog/timespent…
        Action:
            Attachment:
                POST localhost:8080/API/v1/tasks/id/attachments
                DELETE localhost:8080/API/v1/tasks/id/attachments
        



