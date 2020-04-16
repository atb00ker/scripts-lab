using System.Collections.Generic;

namespace useless.Models
{
    public interface ITodoAction
    {
        IEnumerable<Todo> GetAllTodo();
        Todo GetTodo(long Id);
        void AddTodo(Todo TodoAction);
        void UpdateTodo(long Id);
        void DeleteTodo(long Id);
    }
}
