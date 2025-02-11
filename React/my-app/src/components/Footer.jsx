import React from "react";

function Footer(){
    return (
        <div>
            <footer style={styles.footer}>
                <p>&copy;{new Date().getFullYear()}</p>
            </footer>
        </div>
    );
}

const styles = {
    footer : {
        backgroundColor : '#333',
        color : 'white',
        padding : '10px',
        textAlign : 'center',
        position : 'fixed',
        width : '100%',
        bottom : 0  
    }
}

export default Footer;