// console.log("Hello")

// // Q1. 
// // Base Class
// class Employee {
//     constructor(id, name, baseSalary) {
//         this.id = id;
//         this.name = name;
//         this.baseSalary = baseSalary;
//     }

//     calculateSalary() {
//         throw new Error("calculateSalary() must be implemented");
//     }
// }

// // Full-Time Employee
// class FullTimeEmployee extends Employee {
//     constructor(id, name, baseSalary, bonus = 5000) {
//         super(id, name, baseSalary);
//         this.bonus = bonus;
//     }

//     calculateSalary() {
//         return this.baseSalary + this.bonus;
//     }
// }

// // Contract Employee
// class ContractEmployee extends Employee {
//     constructor(id, name, hoursWorked, hourlyRate) {
//         super(id, name, 0);
//         this.hoursWorked = hoursWorked;
//         this.hourlyRate = hourlyRate;
//     }

//     calculateSalary() {
//         return this.hoursWorked * this.hourlyRate;
//     }
// }

// // Commission Employee
// class CommissionEmployee extends Employee {
//     constructor(id, name, totalSales, commissionPercentage = 10) {
//         super(id, name, 0);
//         this.totalSales = totalSales;
//         this.commissionPercentage = commissionPercentage;
//     }

//     calculateSalary() {
//         return this.totalSales * this.commissionPercentage / 100;
//     }
// }

// // Employee Manager
// class EmployeeManager {
//     constructor() {
//         this.employees = [];
//     }

//     addEmployee(employee) {
//         this.employees.push(employee);
//     }

//     calculatePayroll() {
//         let totalPayroll = 0;

//         console.log("Employee Salaries:");
//         this.employees.forEach(emp => {
//             const salary = emp.calculateSalary();
//             console.log(`${emp.id} - ${emp.name}: ${salary}`);
//             totalPayroll += salary;
//         });

//         console.log("--------------------------");
//         console.log("Total Payroll:", totalPayroll);
//     }
// }

// // Main
// const manager = new EmployeeManager();

// manager.addEmployee(new FullTimeEmployee(1, "Alice", 50000));
// manager.addEmployee(new FullTimeEmployee(2, "Bob", 60000, 8000));
// manager.addEmployee(new ContractEmployee(3, "Charlie", 160, 300));
// manager.addEmployee(new CommissionEmployee(4, "David", 200000));
// manager.addEmployee(new CommissionEmployee(5, "Eva", 300000, 15));

// manager.calculatePayroll();

// Q2.

// Custom Exception
class InsufficientBalanceError extends Error {
    constructor(message) {
        super(message);
        this.name = "InsufficientBalanceError";
    }
}

// Abstract Account Class
class Account {
    #balance;

    constructor(balance = 0) {
        this.#balance = balance;
        this.transactions = [];
    }

    getBalance() {
        return this.#balance;
    }

    deposit(amount) {
        this.#balance += amount;
        this.logTransaction(`Deposit: +${amount}`);
    }

    withdraw(amount) {
        if (amount > this.#balance) {
            throw new InsufficientBalanceError("Insufficient Balance!");
        }
        this.#balance -= amount;
        this.logTransaction(`Withdraw: -${amount}`);
    }

    logTransaction(transaction) {
        this.transactions.push(transaction);
        console.log("Ledger:", transaction); // Simulates writing to ledger.txt
    }

    getTransactionHistory() {
        return this.transactions;
    }

    // Simulated recovery
    syncFromLedger() {
        console.log("Recovering account from ledger...");
        console.log("Current Balance:", this.#balance);
    }
}

// Main
const account = new Account(1000);

try {
    account.deposit(500);
    account.withdraw(300);
    account.withdraw(1500); // Throws exception
} catch (error) {
    console.log(error.message);
}

console.log("Balance:", account.getBalance());

console.log("\nTransaction History:");
console.log(account.getTransactionHistory());

