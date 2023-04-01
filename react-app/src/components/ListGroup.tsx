// a new function
import { MouseEvent } from "react";

function ListGroup() {
  let countries = ["Nigeria", "Canada", "USA", "Guinea", "Tokyo"];
  // countries = [];
  // if ((countries = [])) {
  //   return <h1>No Item here</h1>;
  // }

  //to declare a function

  let handleClick = (event: MouseEvent) => console.log(event);
  return (
    //we can use fragment to hold several elements since reat can only return one element
    <>
      <h1>The List</h1>
      {countries.length === 0 && <p>No item found</p>}
      <ul className="list-group">
        {countries.map((country) => (
          <li
            className="list-group-item"
            key={country}
            // onClick={() => {
            //   console.log(country);
            // }}
            //reference function on line 13
            onClick={handleClick}
          >
            {country}
          </li>
        ))}
        {/* <li className="list-group-item">An item</li>
            <li className="list-group-item">A second item</li>
            <li className="list-group-item">A third item</li>
            <li className="list-group-item">A fourth item</li>
            <li className="list-group-item">And a fifth one</li> */}
      </ul>
    </>
  );
}

//export
export default ListGroup;
