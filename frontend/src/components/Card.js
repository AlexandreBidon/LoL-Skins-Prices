// src/components/Card.js
// bg-dark-gray
import React from 'react';

function Card({skin}) {
  return(
    <div className="tc bg-black dib br3 pa0 ma0 grow bw2 shadow-5">
      <img className="br3 w-100 dib" alt={skin.name} src={"http://ddragon.leagueoflegends.com/cdn/img/champion/loading/" + skin.imgPath} />
      <div>
        <h2 className="white">{skin.name}</h2>
        <p className="white">{skin.price}</p>
      </div>
    </div>
  );
}

export default Card;