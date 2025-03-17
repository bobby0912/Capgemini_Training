using System;

public class BankAccount
{
    private decimal balance;

    public BankAccount()
    {
        balance = 0;
    }

    public void Deposit(decimal amount)
    {
        if (amount > 0)
        {
            balance += amount;
            Console.WriteLine($"Deposited: {amount:C}. New balance: {balance:C}");
        }
        else
        {
            Console.WriteLine("Deposit amount must be positive.");
        }
    }

    public void Withdraw(decimal amount)
    {
        if (amount > 0)
        {
            if (balance >= amount)
            {
                balance -= amount;
                Console.WriteLine($"Withdrew: {amount:C}. New balance: {balance:C}");
            }
            else
            {
                Console.WriteLine("Insufficient balance for withdrawal.");
            }
        }
        else
        {
            Console.WriteLine("Withdrawal amount must be positive.");
        }
    }

    public decimal GetBalance()
    {
        return balance;
    }
}