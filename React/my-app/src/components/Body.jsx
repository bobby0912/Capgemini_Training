import React from "react";

function Body(){
    return (
        <main style={styles.main}>
            <h2>welcome to my website</h2>
            <p>this is a sample raect application with a structured layout</p>
        </main>
    );
}

const styles = {
    main : {
        padding : '20px',
        textAlign : 'center'
    }
}

export default Body;