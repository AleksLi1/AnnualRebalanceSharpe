# Annually Rebalanced Max Sharpe Efficient Frontier

This Primary model calculates an efficient frontier of 6 ETF's on an annual basis and selects the portfolio with the highest Sharpe ratio.
In essence, this model looks at the yearly performance of these assets and based on their variance and expected return, and calculates
the weights for the next year.

This is still a work in progress and updates are being pushed regularly. I've also tried my best  to document my code,
so feel free to play around with it and see if there are any improvements that you would suggest. 

Here are the Model 1 results:

![stats](https://i.ibb.co/82wG0yK/model1-2.png)

![Performance](https://i.ibb.co/Tm5n3qt/model-1.png)

![hist](https://i.ibb.co/1nfJTqj/model1-1.png)

In addition, I have included 2 other versions of this model. 

The second version of the first model, Model 2, has the exact same decision-making as Model 1, but has a lookback period
of 6 months instead of an entire year. This has shown to increase portfolio versatility, and as such, achieve much greater
risk-adjusted returns through lower drawdowns. 

Model 2 results:

![Performance](https://i.ibb.co/h98xkRN/Figure-4.png)

![stats](https://i.ibb.co/8DnVNr0/Figure-1.png)

![hist](https://i.ibb.co/VSVNtZ5/Figure-2.png)

For further analysis, I include the following charts that compare Model 1 and Model 2 results.

![P/L1](https://i.ibb.co/FHhmSyz/Picture2.png)

![P/L2](https://i.ibb.co/bdBBXKp/Picture1.png)

As you can see, while Model 1 and Model 2 make almost the same investing decisions, Model 2 was much better at keeping the
returns it had gained, especially during the Coronavirus Crash in 2020. I am now working on further increasing the versatility
of this model by reducing the lookback period to a single quarter. 

Finally, the Primary_GTT model (GTT stands for Growth Trend Timing) uses unemployment data from the FED in an attempt to time the market.
While it incorporates macro theory to determine whether it is a good time to be invested in the market, the previous two models 
have shown that a better way of playing recessions is by being positioned in risk-off assets, rather than sitting on cash.

Primary_GTT results:

![Performance](https://i.ibb.co/yPFgMjp/model-3-1.png)

![stats](https://i.ibb.co/hWwTmng/model-3.png)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact
If you would like to get in touch, my email is aleksandras.v.liauska@bath.edu.

## License
[GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/)