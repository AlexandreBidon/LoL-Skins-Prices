import React from 'react';

class Card1 extends React.Component {
  constructor({skin}) {
    super();
    this.skin = skin;
  }

  render() {
    return (
        <div className="tc bg-black dib br3 pa0 ma0 grow bw2 shadow-5" onClick={this.openModal}>
        <img className="br3 w-100 dib" alt={this.skin.name} src={"http://ddragon.leagueoflegends.com/cdn/img/champion/loading/" + this.skin.imgPath} />
        <div>
          <h2 style={{fontFamily: "Light"}} className="white">{this.skin.name}</h2>
          <p style={{fontFamily: "Light"}} className="white">{this.skin.price} RP</p>
        </div>
      </div>
    );
  }
}

export default Card1;