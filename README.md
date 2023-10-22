# Energy Consumption Calculator

## Overview
The Energy Consumption Calculator is a web-based application built with Flask that allows users to calculate their electricity consumption and cost based on various household devices. Users can input details about the number of devices they use, their usage time, and power consumption to estimate their energy consumption and the associated cost.

## Features
- Calculate energy consumption and cost based on the usage of household devices.
- Users can select from a list of common household devices or add custom devices.
- Provides a breakdown of energy consumption and cost for each device.
- Offers transparency in the calculation of electricity consumption.

## Usage
1. Access the web application through the provided URL.
2. Select or add household devices you want to calculate energy consumption for.
3. Enter the quantity, usage time, and power consumption details for each device.
4. Submit the form to calculate the energy consumption and cost.
5. View the breakdown of energy consumption and cost for each device.

## Calculation Method
The application uses the following calculation method to estimate energy consumption:
- For energy consumption (kWh): `(Quantity * Usage Time * Power Consumption) / 1000`
- The application uses a tiered pricing model to calculate cost based on energy consumption.

## Technology Stack
- Flask: A micro web framework for building web applications.
- HTML/CSS: Front-end web technologies for the user interface.
- SQLite: A lightweight and serverless database for storing device information.
- Python: The programming language used to develop the application.
