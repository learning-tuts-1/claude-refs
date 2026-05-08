---
name: inventory-demand-planning
description: Demand forecasting, safety stock optimization, replenishment planning, and promotional lift estimation for retailers. Use when working on inventory planning, demand forecasts, or stock optimization.
---

# Inventory Demand Planning

Demand planning for multi-location retail — forecasting, safety stock, replenishment.

## Forecasting Methods

| Method | When to Use |
|--------|-------------|
| Moving Averages | Stable demand, low variability, commodity staples |
| Exponential Smoothing (SES) | Stationary demand with noise |
| Holt's (Double) | Items with consistent growth/decline trend |
| Holt-Winters (Triple) | Seasonal items with 52-week/12-month cycles |
| Seasonal Decomposition (STL) | When seasonal patterns shift year over year |
| Causal/Regression | External factors drive demand (price, promos, weather) |
| ML (LightGBM/XGBoost) | 1000+ SKUs, 2+ years history, multiple regressors |

## Accuracy Metrics

- **MAPE** — standard but breaks on low-volume items (<50 units/week)
- **WMAPE** — weighted by actuals, reflects dollars (finance cares about this)
- **Bias** — signed error; < ±5% healthy, >10% means structural problem
- **Tracking Signal** — cumulative error / MAD; >±4 means model drift

## Safety Stock

`SS = Z x sigma_d x sqrt(LT + RP)`

- Z = service level z-score (1.65 for 95%, 2.33 for 99%)
- sigma_d = demand standard deviation per period
- LT = lead time, RP = review period

## ABC/XYZ Classification

| Class | Revenue | Variability | Strategy |
|-------|---------|-------------|----------|
| AX | High | Low | Lean stock, frequent replenishment |
| AY | High | Medium | Safety stock buffer |
| AZ | High | High | High safety stock, close monitoring |
| CZ | Low | High | Consider dropping or make-to-order |

## Promotional Lift

- Separate baseline forecast from promotional uplift
- Encode promo features: depth (% off), display type, circular feature
- Regularize aggressively (Lasso/Ridge) to avoid overfitting on sparse promo history
- Post-promo dip: account for pantry loading effect
