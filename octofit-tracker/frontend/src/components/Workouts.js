import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [data, setData] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const endpoint = codespace
    ? `https://${codespace}-8000.app.github.dev/api/workouts/`
    : 'http://localhost:8000/api/workouts/';

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Workouts endpoint:', endpoint);
        console.log('Workouts data:', results);
      })
      .catch(err => console.error('Workouts fetch error:', err));
  }, [endpoint]);

  return (
    <div className="container mt-4">
      <h2>Workouts</h2>
      <ul className="list-group">
        {data.map((item, idx) => (
          <li key={item.id || idx} className="list-group-item">
            {JSON.stringify(item)}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Workouts;
