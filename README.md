For my publisher and subscriber node program I chose to send battery temperature data in the form of a notification the user can read. It will inform the user about the current state of the battery and display the current temperature. Currently there are two states being when the battery is operating normally and when it has reached a critical temperature (> 35°C).

This type of data is important for robotic systems to ensure user safety and to prevent component damage. By having the battery temperature data available, other subsystems can subscribe to the data and implement it into their safety features. An example of this would be a feature that reduces power to the motors when the battery is at critical temperatures to prevent component damage or a kill switch to shut off the power if the battery could risk being on fire.


<img width="1920" height="1048" alt="tasc_application_terminal" src="https://github.com/user-attachments/assets/5eba6bd1-7797-48a2-92ec-f825fc23d28a" />
<img width="1920" height="1048" alt="tasc_application_rqtgraph" src="https://github.com/user-attachments/assets/67cecfbf-4f52-4c0a-8b2b-66e6bca673f1" />

