using Microsoft.EntityFrameworkCore;
using WebApplication3cake.Models;

namespace WebApplication3cake.Data
{
    public class ExpenseDbContext : DbContext
    {
        public ExpenseDbContext(DbContextOptions<ExpenseDbContext> options) : base(options) { }

        public DbSet<Expense> Expenses { get; set; }
    }
}
