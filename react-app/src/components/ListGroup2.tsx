import { useState } from "react";

function ListGroup2() {
  let countries = ["Nigeria", "Canada", "South Africa"];
  let selected_item = 0;
  const [selectedIndex, setSelectedIndex] = useState(-1);

  //lets render it

  return (
    <>
      <h1>Hello There</h1>
      <ul className="list-group">
        {countries.map((country, index) => (
          <li
            onClick={() => setSelectedIndex(index)}
            className={
              selectedIndex === index
                ? "list-group-item active"
                : "list-group-item"
            }
            key={country}
          >
            {country}
          </li>
        ))}
      </ul>
    </>
  );
}

//make it exportable
export default ListGroup2;
