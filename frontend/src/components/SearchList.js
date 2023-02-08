// src/components/SearchList.js

import React from 'react';
import Card1 from './Card1';

function SearchList({ filteredPersons }) {
  const filtered = filteredPersons.map(skin =>  <Card1 key={skin.id} skin={skin} />); 
  return (
    <div>
      {filtered}
    </div>
  );
}

export default SearchList;