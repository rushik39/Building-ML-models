**Objective**
The goal of this project was to build a linear regression model to predict Sales based on advertising spend across different media channels: TV, Radio, and Newspaper.

**Dataset Overview**
The dataset contains advertising expenditure data and corresponding sales figures. 

The features include:
1. TV: Advertising spend on television (in thousands of dollars)
2. Radio: Advertising spend on radio
3. Newspaper: Advertising spend on newspaper

Sales: Target variable

**Preprocessing**
Loaded the data using pandas and inspected it using .head(), .describe(), and .info().
Selected the features (TV, Radio, Newspaper) as x and the target (Sales) as y.

**Note: **
While I explored scaling techniques like Min-Max Scaling and Standardization, I did not apply them in this case because scikit-learn’s LinearRegression model does not require feature scaling. However, I learned that:

1. Min-Max Scaling is a method of normalizing data by transforming values into a fixed range, typically between 0 and 1. This is useful when features have different units or scales and you want them to be treated equally by the model.

2. Standardization (Z-score normalization) transforms the data to have a mean of 0 and a standard deviation of 1. It is especially useful when the data is normally distributed or when the model assumes a Gaussian distribution. Standardization helps ensure that features with different ranges (e.g., one ranging from 1–1000 and another from 1–10) are comparable by measuring how far each value is from the mean in standard deviations.

Next I split the dataset into training and testing sets:

80% of the data was used for training, and 20% for testing.

Fitted a linear regression model using scikit-learn

Predicted values for the test set and evaluated performance using:
1. Mean Squared Error (MSE): Measures average squared difference between actual and predicted values.
2. R-squared (R²): Measures how well the model explains the variance in the target.
3. r (Correlation Coefficient): The correlation coefficient measures how strongly the predicted values are linearly related to the actual values. A value close to 1 indicates a strong positive correlation, meaning the predictions closely follow the actual data.
While r is not a direct measure of error like MSE, it gives insight into the strength and direction of the linear relationship between the model’s predictions and actual outcomes. In simple linear regression, a strong correlation typically indicates that the model has good predictive ability.

**Conclusion:**
The linear regression model was effective in predicting Sales based on advertising spend. The evaluation metrics indicate a good fit with MSE being 2.9, r being 0.95 and R² being 0.906, and the process gave hands-on experience with model training, validation, and performance interpretation.
