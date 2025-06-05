from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>📝 Task Manager API</h1>
        <p>This is a simple CRUD app built with Django Rest Framework.</p>
        <ul>
            <li>GET /api/task/ – List all tasks</li>
            <li>POST /api/task/ – Create a task</li>
            <li>PUT /api/task/&lt;id&gt;/ – Toggle completion</li>
            <li>DELETE /api/task/&lt;id&gt;/ – Delete a task</li>
        </ul>
    """)
