// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Counter {
    uint256 public counter;

    constructor() {
        counter = 0;
    }

    function count() public {
        counter = counter + 1;
    }

    function add(uint value) public returns (uint){
        counter = counter + value;
        return counter;
    }

    function get() public view returns (uint) {
        return counter;
    }
}
