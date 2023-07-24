import React from 'react';
import axios from 'axios';

function App() {
  
  // Hooks
  const [todos, setTodos] = React.useState([]);

  // Axios call
  const getTodos = () => {
    axios.get('/api/').then(res => {
      setTodos(res.data);
    })
    .catch(err => {
      console.log(err);
    });
  }

  // Call getTodos on component mount
  React.useEffect(() => {
    getTodos();
  }, []);

  return (
    <div>
      <h1>My todos:</h1>
      {todos.map(item => (
        <div key={item.id} style={{paddingLeft: '1%'}}>
          <h1>{item.title}</h1>
          <span>{item.body}</span>
        </div>
      ))}
    </div>        
  );
}

export default App;
