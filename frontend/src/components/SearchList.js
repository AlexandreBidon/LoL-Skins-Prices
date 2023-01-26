// src/components/SearchList.js

import React from 'react';
import Card from './Card';

function SearchList({ filteredPersons }) {
  const filtered = filteredPersons.map(skin =>  <Card key={skin.id} skin={skin} />); 
  return (
    <div>
      {filtered}
    </div>
  );
}

export default SearchList;