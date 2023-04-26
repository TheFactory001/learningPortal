import { useState } from "react";
import ExpenseList from "./components/ExpenseList";
import Form from "./components/Form";
import ExpenseFilter from "./components/ExpenseFilter";
import ExpenseForm from "./components/ExpenseForm";

export const categories = ["", "Cheese", "Drinks", "Beverages"];

function App() {
  // const sample_expenses = [
  //   { id: 1, description: "Hangrup", amount: 5000, category: "Cheese" },
  //   { id: 2, description: "Hangrup", amount: 5000, category: "Cheese" },
  //   { id: 3, description: "Hangrup", amount: 5000, category: "Cheese" },
  // ];

  const [expenseItems, setExpenseItems] = useState([
    { id: 1, description: "Hangrup", amount: 5000, category: "Cheese" },
    { id: 2, description: "Hangrup", amount: 5000, category: "Cheese" },
    { id: 3, description: "Hangrup", amount: 5000, category: "Cheese" },
    { id: 4, description: "Fanta", amount: 5000, category: "Drinks" },
  ]);
  const [selectedCategory, setSelectedCategory] = useState("");

  const handleDeleteButton = (id: number) => {
    console.log("Deleted expense" + id);
    setExpenseItems(expenseItems.filter((expense) => id != expense.id));
  };

  //filter and only pass visble items in the Expense list
  const visibleExpenses = selectedCategory
    ? expenseItems.filter((expense) => expense.category === selectedCategory)
    : expenseItems;
  return (
    <div>
      <div className="mb-5">
        <ExpenseForm
          addExpense={(sampleElement) => {
            console.log(sampleElement);
            setExpenseItems([
              ...expenseItems,
              {
                ...sampleElement,
                amount: Number(sampleElement.amount),
                id: expenseItems.length + 1,
              },
            ]);
          }}
        />
      </div>

      <div className="mb-3">
        <ExpenseFilter
          onSelectCategory={(category) => {
            setSelectedCategory(category);
          }}
        />
      </div>
      <ExpenseList
        expenses={visibleExpenses}
        onDeleteExpense={(id) => handleDeleteButton(id)}
      />
    </div>
  );
}

export default App;
