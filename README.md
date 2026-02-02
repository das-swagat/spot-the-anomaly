# Spot the Anomaly

A minimal interactive experiment.

A time series is briefly shown without annotations.  
You estimate where a deviation occurs.  
Your estimate is compared against a simple **self-supervised anomaly score**,  
followed by a visual reveal.

This is not a trained self-supervised learning (SSL) model.  
It is a lightweight demonstration of the core self-supervised idea: using local context as the supervisory signal, without labels.

---

## Run

Clone the repository and execute the script:

```bash
git clone https://github.com/das-swagat/spot-the-anomaly
cd spot-the-anomaly
python3 spot_the_anomaly.py
```

**The script will:**
1. Display a time series for a few seconds
2. Prompt for an index estimate
3. Report the user estimate, model estimate, and true location
4. Show a plot highlighting all three

**Notes**
1. The data is synthetic.
2. No labels are used.
3. The scoring rule relies only on local context.
4. The intent is intuition, not optimal detection.
