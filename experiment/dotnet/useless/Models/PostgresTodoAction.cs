using System.Collections.Generic;
using System.Linq;

namespace useless.Models
{
    public class PostgresTodoAction : ITodoAction
    {

        private readonly TodoDbContext context;
        public PostgresTodoAction(TodoDbContext context)
        {
            this.context = context;
        }
        public IEnumerable<Todo> GetAllTodo()
        {
            return context.Todo.OrderBy(obj => obj.Id);
        }
        public Todo GetTodo(long Id)
        {
            return context.Todo.Find(Id);
        }
        public void AddTodo(Todo TodoAction)
        {
            var lastTodo = context.Todo.OrderBy(obj => obj.Id).Last();
            TodoAction.Id = lastTodo.Id + 1;
            context.Todo.Add(TodoAction);
            context.SaveChanges();
        }
        public void UpdateTodo(long Id)
        {
            Todo todoAction = context.Todo.Find(Id);
            if (todoAction != null)
            {
                todoAction.IsComplete = !todoAction.IsComplete;
                var change = context.Todo.Attach(todoAction);
                change.State = Microsoft.EntityFrameworkCore.EntityState.Modified;
                context.SaveChanges();
            }
        }

        public void DeleteTodo(long Id)
        {
            Todo todoAction = context.Todo.Find(Id);
            if (todoAction != null)
            {
                context.Todo.Remove(todoAction);
                context.SaveChanges();
            }
        }
    }
}
