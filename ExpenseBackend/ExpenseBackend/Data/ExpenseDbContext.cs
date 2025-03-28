using Microsoft.EntityFrameworkCore;
using ExpenseBackend.Models;

namespace ExpenseBackend.Data
{
    public class ExpenseDbContext : DbContext
    {
        public ExpenseDbContext(DbContextOptions<ExpenseDbContext> options) : base(options) { }

        public DbSet<Expense> Expenses { get; set; }
    }
}
