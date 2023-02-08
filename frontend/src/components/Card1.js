import React from 'react';
import ReactDOM from 'react-dom';
import Modal from 'react-modal';

const customStyles = {
  content : {
    top                   : '50%',
    left                  : '50%',
    right                 : 'auto',
    bottom                : 'auto',
    marginRight           : '-50%',
    transform             : 'translate(-50%, -50%)'
  }
};

// Make sure to bind modal to your appElement (http://reactcommunity.org/react-modal/accessibility/)
Modal.setAppElement('#yourAppElement')

class Card1 extends React.Component {
  constructor({skin}) {
    super();

    this.state = {
      modalIsOpen: false
    };

    this.skin = skin;
    this.openModal = this.openModal.bind(this);
    this.afterOpenModal = this.afterOpenModal.bind(this);
    this.closeModal = this.closeModal.bind(this);
  }

  openModal() {
    this.setState({modalIsOpen: true});
  }

  afterOpenModal() {
    // references are now sync'd and can be accessed.
    this.subtitle.style.color = '#f00';
  }

  closeModal() {
    this.setState({modalIsOpen: false});
  }

  render() {
    return (
        <div className="tc bg-black dib br3 pa0 ma0 grow bw2 shadow-5" onClick={this.openModal}>
        <Modal
          isOpen={this.state.modalIsOpen}
          onAfterOpen={this.afterOpenModal}
          onRequestClose={this.closeModal}
          style={customStyles}
          contentLabel="Example Modal"
        ></Modal>
        <img className="br3 w-100 dib" alt={this.skin.name} src={"http://ddragon.leagueoflegends.com/cdn/img/champion/loading/" + this.skin.imgPath} />
        <div>
          <h2 className="white">{this.skin.name}</h2>
          <p className="white">{this.skin.price}</p>
        </div>
      </div>
    );
  }
}

export default Card1;