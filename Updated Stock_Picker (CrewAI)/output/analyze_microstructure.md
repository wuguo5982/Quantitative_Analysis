Below is a **microstructure evidence table** separating **observed**, **modeled**, and **unavailable** evidence for the requested signals.

## Scope / caveats
- **Reporting lags matter**:
  - **FINRA ATS / TRF** prints are **reported after the fact** and should be treated as lagged microstructure evidence, not real-time flow.
  - **Options open interest** is **end-of-day / delayed** and changes with reporting cycles.
  - **ETF flow** data from SEC fund filings is **monthly/quarterly lagged**, not same-day flow.
- **GEX and gamma flip are estimates**:
  - They are **modeled from options positioning / open interest / dealer-assumption frameworks**, not directly observed dealer inventories.
- I did **not** use current price claims.
- I did **not** assert any hidden dealer position as fact.

---

# Microstructure table: observed vs modeled vs unavailable

| Signal | What is actually observed / verifiable | What is modeled / inferred | What is unavailable / not directly observable | Practical interpretation |
|---|---|---|---|---|
| **FINRA ATS volume** | FINRA publishes aggregated ATS transparency data. Official FINRA ATS transparency pages indicate ATS data is reported in aggregated form, with quarterly statistics available. Source basis: FINRA OTC Transparency / ATS Quarterly Statistics. | Analysts may infer off-exchange participation, venue share shifts, and liquidity migration trends from ATS prints. | Real-time ATS motives, parent order intent, and beneficial owner identity are unavailable. | Useful for identifying persistent off-exchange liquidity trends, but not for attributing intent. |
| **FINRA TRF volume** | FINRA TRF is the official mechanism for reporting OTC equity trades executed away from exchanges. Official FINRA TRF pages and trade-reporting resources confirm the facility structure. | Off-exchange share, internalization trends, and execution timing patterns can be inferred from TRF aggregate behavior. | The initiating trader’s intent, strategy, and exact dealer inventory effect are unavailable. | Good for broad lit/off-exchange vs off-exchange venue analysis, but delayed and incomplete for causal claims. |
| **Options skew** | Cboe publishes official SKEW index dashboard. This is a directly observed market index derived from SPX option prices. Official Cboe dashboard shows the SKEW level. | Tail-risk perception, crash-premium demand, and convexity pricing are inferred from skew behavior. | Specific investor identity and exact hedger motivation are unavailable. | High skew implies higher demand for downside protection or tail hedging, but not necessarily imminent downside. |
| **Put/call ratio** | Cboe publishes official U.S. options daily market statistics including total, index, ETF, and equity put/call ratios. | Sentiment interpretation is inferred: higher put/call can indicate defensive positioning; lower can indicate risk-on behavior. | Whether the flow is hedging, speculation, or overwriting is not directly observable from the ratio alone. | Useful sentiment gauge, but very noisy without segmentation by index vs equity vs ETF options. |
| **Implied volatility (IV)** | IV is directly observable from listed option prices and official market data products. | Forward risk expectations, event premia, and relative richness/cheapness are modeled from IV term structure and surface. | The exact ex-ante reason for elevated IV is unavailable from the quote alone. | Strong for identifying event risk and relative option richness, but not sufficient to infer direction. |
| **Options volume / open interest** | Cboe and OCC publish volume and open interest reports. OCC open-interest data is explicitly available in market data reports. | Position buildup, crowding, strike concentration, and potential pinning zones are inferred. | The side of the trade, beneficial owner, and whether it is opening vs closing for every participant are not fully observable. | High OI at key strikes can matter for gamma sensitivity, but interpretation requires caution. |
| **ETF flows** | SEC Form N-PORT and SEC registered-fund flow pages provide official fund reporting, but with reporting delay. | Net creation/redemption pressure, sector rotation, and passive allocation changes are inferred. | True same-day AP basket activity and intraday primary market flow are not directly observable from these filings. | Useful for medium-horizon flow trends, not for intraday execution timing. |
| **GEX (gamma exposure)** | Not directly observed as a market-reported metric. | Must be estimated from options OI, IV, moneyness, and dealer assumptions. | Actual dealer books, hedge ratios, and live inventory are unavailable. | Use only as a model output; do not treat as factual positions. |
| **Gamma flip** | Not directly observed as a published market statistic. | Estimated from the point where dealer gamma changes sign in the model. | The exact dealer positioning threshold is unavailable. | Best treated as an estimated regime marker, not a confirmed market level. |

---

# Evidence by signal type

## 1) FINRA ATS / TRF
### Observed
- FINRA provides official ATS transparency and TRF infrastructure.
- FINRA states ATS trade data is aggregated in its transparency framework.
- FINRA TRF is the official reporting venue for OTC equity transactions.

### Modeled
- Off-exchange share
- Internalization intensity
- Venue migration / fragmentation
- Liquidity concentration by time of day or security bucket

### Unavailable
- True beneficial owner
- Dealer inventory
- Parent order intent
- Whether a print was hedging, facilitation, or speculative internalization

### Important lag note
- ATS / TRF prints are **not real-time evidence of current positioning**.
- They are best used as **post-trade microstructure context**.

---

## 2) Options skew
### Observed
- Cboe’s official **SKEW Index dashboard** provides the observed index level.
- This is a market-derived measure based on SPX option prices.

### Modeled
- Tail-risk premium
- Crash-protection demand
- Risk asymmetry
- Relative cheapness/richness of downside hedges

### Unavailable
- The identity of hedgers
- Whether demand came from institutions, systematic funds, or speculators
- Whether elevated skew reflects fear, portfolio insurance, or tactical event hedging

---

## 3) Put/call
### Observed
- Cboe publishes:
  - total put/call
  - index put/call
  - ETF put/call
  - equity put/call

### Modeled
- Market sentiment
- Hedging intensity
- Speculative risk appetite
- Relative demand for downside vs upside convexity

### Unavailable
- Whether puts are protective or directional
- Whether calls are covered, synthetic, or outright bullish
- Whether the flow is single-name or index-driven after netting

---

## 4) Implied volatility
### Observed
- IV is directly derived from option prices.
- It is a market-implied forward measure.

### Modeled
- Earnings/event premium
- Forward uncertainty
- Volatility term structure
- Relative vol rank / percentile
- Skewed distribution expectations

### Unavailable
- Exact catalyst attribution
- Whether IV is driven by dealer hedging, customer demand, or arbitrage
- True realized path before the event occurs

---

## 5) Volume / open interest
### Observed
- OCC / exchange data provide volume and open interest.
- This is directly reported market data.

### Modeled
- Position concentration
- Pin risk
- Dealer hedging sensitivity
- Strike magnetism
- Gamma clustering

### Unavailable
- Opening vs closing intent for all participants
- Dealer directional positioning
- Whether OI is long or short at the customer level

---

## 6) ETF flows
### Observed
- SEC fund reporting and registered-fund flow data are official sources.
- These are lagged and aggregated.

### Modeled
- Sector rotation
- Persistent inflows/outflows
- Passive demand support or supply pressure

### Unavailable
- Intraday creation/redemption details in real time
- Exact AP inventory
- Beneficial-owner attribution

---

# Signal quality ranking by observability

## Highest observability
1. **Options volume**
2. **Open interest**
3. **Put/call ratio**
4. **SKEW / IV surface**
5. **FINRA ATS / TRF aggregate prints**
6. **ETF flows**
7. **GEX**
8. **Gamma flip**

## Why
- The first four are either directly published or derived from directly observed exchange data.
- ATS/TRF are published but lagged and aggregated.
- ETF flows are official but delayed.
- GEX and gamma flip are **model outputs**, not observed market facts.

---

# Best-practice interpretation framework

## Use as observed evidence
- FINRA ATS / TRF aggregates
- Cboe put/call ratios
- Cboe SKEW
- OCC / exchange volume and open interest
- SEC fund flow datasets

## Use as modeled evidence only
- GEX
- Gamma flip
- Dealer positioning proxies
- Pinning / magnetization levels

## Treat as unavailable / not inferable
- Real-time dealer books
- Beneficial ownership of flow
- Motivations behind each trade
- Exact hedge ratios per participant
- Same-day ETF primary-market execution details from public filings alone

---

# Practical conclusion
The verifiable evidence stack is strongest when you separate:
- **Observed market structure**: ATS/TRF prints, options volume, OI, put/call, skew, IV
- **Lagged fund-flow evidence**: ETF flows via SEC reporting
- **Modeled derivatives positioning**: GEX and gamma flip

So the correct analytic posture is:

- **Observed** = what the market reported
- **Modeled** = what may be inferred from reported data
- **Unavailable** = what cannot be directly verified from public microstructure data

If you want, I can convert this into a **ticker-by-ticker microstructure worksheet** for the 50-name universe, with columns for:
- ATS/TRF relevance
- options liquidity
- skew sensitivity
- put/call usefulness
- IV regime
- OI concentration
- ETF flow relevance
- GEX / gamma-flip reliability