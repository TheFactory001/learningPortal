import React from "react";
import { categories } from "../App";
interface Props {
  onSelectCategory: (category: string) => void;
}
const ExpenseFilter = ({ onSelectCategory }: Props) => {
  interface Expenses {
    id: number;
    description: string;
    amount: number;
    category: string;
  }

  return (
    <>
      <div>
        <select
          className="form-select"
          name=""
          id=""
          onChange={(event) => {
            onSelectCategory(event.target.value);
          }}
        >
          <option value="">All Categories</option>
          {categories.map((category) => (
            <option value={category} key={category}>
              {category}
            </option>
          ))}
        </select>
      </div>
    </>
  );
};

export default ExpenseFilter;
