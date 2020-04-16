using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using useless.Models;

namespace useless.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        private readonly ITodoAction _database;
        public HomeController(ITodoAction database, ILogger<HomeController> logger)
        {
            _logger = logger;
            _database = database;
        }

        public IActionResult Index()
        {
            return View();
        }

        public IActionResult Privacy()
        {
            return View();
        }

        [HttpGet]
        public IActionResult Crud(long Id, bool update = false, bool delete = false)
        {
            if (delete == true)
            {
                _database.DeleteTodo(Id);
                return RedirectToAction("crud");
            }
            else if (update == true)
            {
                _database.UpdateTodo(Id);
                return RedirectToAction("crud");
            }
            else
            {
                ViewBag.TodoVal = _database.GetAllTodo();
                return View();
            }
        }

        [HttpPost]
        public IActionResult Crud(Todo TodoVal)
        {
            if (ModelState.IsValid)
            {
                _database.AddTodo(TodoVal);
                return RedirectToAction("crud");
            }
            ViewBag.TodoVal = _database.GetAllTodo();
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
