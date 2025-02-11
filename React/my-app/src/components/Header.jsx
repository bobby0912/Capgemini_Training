import React from "react";

function Header(){
    return (
        <header style={styles.header}>
            <h1>My Website!</h1>
            <nav>
                <ul style={styles.navList}>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">About</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
            </nav>

        </header>
    );
}

const styles = {
    header:{
        backgroundColor : '#333',
        color : 'white',
        padding : '10px',
        textAlign : 'center'
    },
    navList:{
        listStyleType:'none',
        padding : 0,
        display : 'flex',
        justifyContent : 'center'
    }
}

export default Header;