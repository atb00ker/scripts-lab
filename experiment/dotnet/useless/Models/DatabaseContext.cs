using Microsoft.EntityFrameworkCore;

namespace useless.Models {
    public class TodoDbContext : DbContext {
        public TodoDbContext (DbContextOptions<TodoDbContext> options) : base (options) { }
        public DbSet<Todo> Todo { get; set; }
    }
}
