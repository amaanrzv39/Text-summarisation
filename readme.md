# Project Description
Transformer-based models have gained immense popularity due to their ability to understand and process natural language efficiently. These models create high-level linguistic and semantic representations by leveraging unsupervised pre-training on large text datasets using masked language modeling (MLM).

In this project, I implement text summarization using Facebook's BART model, which is designed for sequence-to-sequence tasks. Unlike traditional transformer models, BART is pre-trained using both MLM (masked language modeling) and NSP (next-sentence prediction), making it highly effective for summarization.

### Features:
✅ Load and fine-tune the BART model on a summarization dataset<br>
✅ Utilize the Hugging Face Hub API for model access<br>
✅ Use PyTorch for deep learning implementation<br>
✅ Track and visualize training with Weights & Biases<br>
✅ Evaluate performance using the ROUGE score<br>

This project provides a FastAPI backend that allows users to input text and generate summaries efficiently. 🚀

## Project Structure
```
Text-summarisation/
│── dataset                 # BBC articles csv data
│── notebook                # contains implementation notebook
│── app.py                  # FastAPI application
│── models.py               # define data models using Pydantic
│── requirements.txt        # Dependencies

```

## How to Run
1. Clone repo
```
git clone https://github.com/amaanrzv39/Text-summarisation.git
cd Text-summarisation
```
2. Create virtual environment
```
python -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate      # For Windows
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Start app
```
uvicorn app:app --reload
```
5. Test app
```
curl -X 'POST' 'http://127.0.0.1:8000/summarize' \
     -H 'Content-Type: application/json' \
     -d '{
           "text": "High fuel prices hit BA'\''s profits\n\nBritish Airways has blamed high fuel prices for a 40% drop in profits.\n\nReporting its results for the three months to 31 December 2004, the airline made a pre-tax profit of £75m ($141m) compared with £125m a year earlier. Rod Eddington, BA'\''s chief executive, said the results were \"respectable\" in a third quarter when fuel costs rose by £106m or 47.3%. BA'\''s profits were still better than market expectation of £59m, and it expects a rise in full-year revenues.\n\nTo help offset the increased price of aviation fuel, BA last year introduced a fuel surcharge for passengers.\n\nIn October, it increased this from £6 to £10 one-way for all long-haul flights, while the short-haul surcharge was raised from £2.50 to £4 a leg. Yet aviation analyst Mike Powell of Dresdner Kleinwort Wasserstein says BA'\''s estimated annual surcharge revenues - £160m - will still be way short of its additional fuel costs - a predicted extra £250m. Turnover for the quarter was up 4.3% to £1.97bn, further benefiting from a rise in cargo revenue. Looking ahead to its full year results to March 2005, BA warned that yields - average revenues per passenger - were expected to decline as it continues to lower prices in the face of competition from low-cost carriers. However, it said sales would be better than previously forecast. \"For the year to March 2005, the total revenue outlook is slightly better than previous guidance with a 3% to 3.5% improvement anticipated,\" BA chairman Martin Broughton said. BA had previously forecast a 2% to 3% rise in full-year revenue.\n\nIt also reported on Friday that passenger numbers rose 8.1% in January. Aviation analyst Nick Van den Brul of BNP Paribas described BA'\''s latest quarterly results as \"pretty modest\". \"It is quite good on the revenue side and it shows the impact of fuel surcharges and a positive cargo development, however, operating margins down and cost impact of fuel are very strong,\" he said. Since the 11 September 2001 attacks in the United States, BA has cut 13,000 jobs as part of a major cost-cutting drive. \"Our focus remains on reducing controllable costs and debt whilst continuing to invest in our products,\" Mr Eddington said. \"For example, we have taken delivery of six Airbus A321 aircraft and next month we will start further improvements to our Club World flat beds.\" BA'\''s shares closed up four pence at 274.5 pence.",
           "min_length": 30,
           "max_length": 100
         }'

```
6. Response Format
```
{"summary":" Erel Avineri, executive of AARA, said the results were \"respectable\" in a third quarter when fuel costs rose by £106m or 47.3%.Since the 11 September 2001 attacks in the United States, BA has cut 13,000 jobs as part of a major cost-cutting drive.\"For the year to March 2005, the total revenue outlook is slightly better than previous guidance with a 3% to 3.5% improvement anticipated,\" BA chairman Martin B"}
```

# 📜 License

This project is open-source and available under the MIT License.