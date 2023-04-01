
//create the first component

function FirstMessage(){
    //JSX: JavaScript XML
    const name = 'Daniel';
    if (name.length<7){
        return <h1>Hello {name}</h1>;
    }
    else {
        return <h1>Hello World</h1>
    }
    
}

//export it to make it reusable
export default FirstMessage;

