using System.Collections.Generic;
using System.Linq;

namespace useless.Models
{
    public class MockTodoAction : ITodoAction
    {
        List<Todo> TodoList = new List<Todo>();
        public MockTodoAction()
        {
            TodoList.Add(new Todo() { Id = 1, Name = "1", IsComplete = false });
            TodoList.Add(new Todo() { Id = 2, Name = "2", IsComplete = false });
            TodoList.Add(new Todo() { Id = 3, Name = "3", IsComplete = false });
            TodoList.Add(new Todo() { Id = 4, Name = "4", IsComplete = false });
            TodoList.Add(new Todo() { Id = 5, Name = "5", IsComplete = false });
        }

        public IEnumerable<Todo> GetAllTodo()
        {
            return TodoList.OrderBy(obj => obj.Id);
        }
        public Todo GetTodo(long Id)
        {
            return TodoList.Find(obj => obj.Id == Id);
        }

        public void AddTodo(Todo TodoAction)
        {
            var lastTodo = TodoList.OrderBy(obj => obj.Id).Last();
            TodoAction.Id = lastTodo.Id + 1;
            TodoList.Add(TodoAction);
        }
        public void UpdateTodo(long Id)
        {
            Todo changeItem = TodoList.Find(obj => obj.Id == Id);
            TodoList.Remove(changeItem);
            changeItem.IsComplete = true;
            TodoList.Insert((int)Id, changeItem);
        }

        public void DeleteTodo(long Id)
        {
            Todo removeItem = TodoList.Find(obj => obj.Id == Id);
            TodoList.Remove(removeItem);
        }
    }
}
