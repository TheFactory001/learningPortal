import React from "react";
interface Expenses {
  id: number;
  description: string;
  amount: number;
  category: string;
}
interface Props {
  expenses: Expenses[];
  onDeleteExpense: (id: number) => void;
}
const ExpenseList = ({ expenses, onDeleteExpense }: Props) => {
  if (expenses.length === 0) {
    return null;
  }
  return (
    <>
      <table className="table table-bordered">
        <thead>
          <tr>
            <th>Description</th>
            <th>Amount</th>
            <th>Category</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {expenses.map((expense) => (
            <tr key={expense.id}>
              <td>{expense.description}</td>
              <td>{expense.amount}</td>
              <td>{expense.category}</td>
              <td>
                <button
                  className="btn btn-outline-danger"
                  onClick={() => onDeleteExpense(expense.id)}
                >
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
        <tfoot>
          <tr>
            <td>Total</td>
            <td>
              {/* getting total of the expenses - it works like a loop, goes over every item in the iterable and gets the accumulated value */}
              {expenses
                .reduce((acc, expense) => expense.amount + acc, 0)
                .toFixed(2)}
            </td>
            <td></td>
            <td></td>
          </tr>
        </tfoot>
      </table>
    </>
  );
};

export default ExpenseList;
