import React, { useRef } from "react";
import { useForm } from "react-hook-form";
import { categories } from "../App";
import { z } from "zod";
interface ExpenseData {
  description: string;
  amount: number;
  category: string;
}
interface Props {
  addExpense: (sampleExpense: ExpenseData) => void;
}
// interface Props {
//   categories: string[];

//  addExpense =()
// }

const ExpenseForm = ({ addExpense }: Props) => {
  const { register, handleSubmit } = useForm<ExpenseData>();

  // const nameRef = useRef(null);
  return (
    <>
      <form action="" onSubmit={handleSubmit(addExpense)}>
        <div className="mb-3">
          <label htmlFor="description" className="form-label">
            Description
          </label>

          <input
            {...register("description")}
            type="text"
            id="description"
            className="form-control"
          />
        </div>
        <div className="mb-3">
          <label htmlFor="amount" className="form-label">
            Amount
          </label>

          <input
            {...register("amount")}
            type="text"
            id="Amount"
            typeof="number"
            className="form-control"
          />
        </div>

        <div className="mb-3">
          <label htmlFor="category" className="form-label">
            Category
          </label>

          <select
            {...register("category")}
            className="form-select"
            id="category"
          >
            {/* <option value=""></option> */}
            {categories.map((category) => (
              <option value={category} key={category}>
                {category}
              </option>
            ))}
          </select>
        </div>
        <div className="mb-3">
          {" "}
          <button
            className="btn btn-primary"
            // onClick={(e) => {
            //   e.preventDefault();
            //   console.log(nameRef);
            // }}
          >
            Add Item
          </button>
        </div>
      </form>
    </>
  );
};

export default ExpenseForm;
