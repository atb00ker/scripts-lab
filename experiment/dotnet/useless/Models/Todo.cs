using System.ComponentModel.DataAnnotations;

namespace useless.Models {
    public class Todo {

        [Key]
        public long Id { get; set; }

        [Required]
        public string Name { get; set; }
        public bool IsComplete { get; set; }
    }
}
