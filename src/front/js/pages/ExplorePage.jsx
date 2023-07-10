import React, { useContext, useEffect } from "react";
import { Context } from "../store/appContext";
import { Card } from "../component/Card";

const ExplorePage = () => {
  const {  store } = useContext(Context);
  const { ilustrationData} = store;
  

  

  return (
    <>
      <div className="container">
        <div className="input-group my-3">
          <span className="input-group-text" id="inputGroup-sizing-default">
            Busqueda
          </span>
          <input
            type="text"
            className="form-control"
            aria-label="Sizing example input"
            aria-describedby="inputGroup-sizing-default"
            placeholder="que tipo de imagen estas buscando?"
          />
        </div>

        <div className="row">
          {store.ilustrationData.map((ilustration) => 
             (
              <Card
                key={ilustration.id}
                title={ilustration.title}
                description={ilustration.description}
                image={ilustration.image}
                user={ilustration.user.name}
                id={ilustration.id}
              />              
            ))}
        </div>
      </div>
    </>
  );
};

export default ExplorePage;

