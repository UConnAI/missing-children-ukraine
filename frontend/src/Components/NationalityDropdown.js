import React from "react";

function NationalityDropdown(props) {
    return(
        <select value={this.state.value} onChange={this.handleChange}>
            <option value="ukr">Ukrainian</option>
            <option value="pol">Polish</option>
        </select>
    );
}

export default NationalityDropdown;