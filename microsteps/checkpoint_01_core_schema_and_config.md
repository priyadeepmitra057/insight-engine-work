# CHECKPOINT 01: Core Schema and Config
Directly modified:   schema.py, config.py
Indirectly affected: All modules importing Col
Code blocks used:    CB-P1-01, CB-P1-11
Risk:                HIGH
Depends on:          NONE

---
EXECUTOR DIRECTIVE
You are an executor. Not a decision maker.
Follow each step exactly as written.
Do not infer. Do not improvise. Do not skip.
Do not reformat or alter any code block.
If a step is unclear → STOP and ask.
If a pre-condition fails → STOP and report.
If any validation fails → STOP. Do not continue.
Never modify files not listed in the current step.
Confirm each step complete before moving to next.
Treat every silent success as a potential silent failure until validation proves otherwise.
Never self-fix a failed test. HALT and wait for instruction.
---

CONTEXT
Updating the core schema to include passion-related columns and migrating `TIP_CORPUS` in `config.py` to the new structured schema required by the passion engine.

PRE-CONDITIONS
[ ] Codebase is in original state.

STEPS

  STEP [1.1]
  File:           schema.py
  Action:         MODIFY
  Target:         Col class
  Source file:    passion_plan_part1.md
  Source section: 1. schema.py Update
  Block ID:       CB-P1-01
  Flags:          NONE

  Before:
  ```python
    # ── ML Insight Engine (benchmark / training) ──────────────────────────
    CATEGORY_CONFIDENCE = "category_confidence"
    INSIGHT_TYPE = "insight_type"
    TIP_ID = "tip_id"
    INSIGHT_SCORE = "insight_score"
  ```

  Instruction: Insert the two new constants after the `INSIGHT_SCORE` line.

  After:
  ```python
    # ── Passion Engine: Subcategory Inference ─────────────────────────────
    INFERRED_SUBCATEGORY   = "inferred_subcategory"
    SUBCATEGORY_CONFIDENCE = "subcategory_confidence"
  ```

  Rollback: Remove the two added lines.

  STEP [1.2]
  File:           config.py
  Action:         MODIFY
  Target:         TIP_CORPUS and SPECIFIC_MERCHANT_ALIASES
  Source file:    passion_plan_part1.md
  Source section: 7a. config.py — TIP_CORPUS Schema Migration
  Block ID:       CB-P1-11
  Flags:          [INTERFACE BREAK RISK]

  Before:
  ```python
TIP_CORPUS: dict[str, dict] = {
    # ── Food ──────────────────────────────────────────────────────────────────
    "tip_food_spike_01": {
        "text": "A single ₹500 meal substitution per week could save ~₹2,000/month.",
        "categories": ["food"],
        "insights": ["spending_spike"],
    },
    "tip_food_spike_02": {
        "text": "This food expense is significantly above your average. "
                "Consider splitting large orders or using offers/coupons.",
        "categories": ["food"],
        "insights": ["spending_spike"],
    },
    "tip_food_trend_01": {
        "text": "Your food spending has been rising week over week. "
                "Try batch-cooking on weekends to reduce delivery dependency.",
        "categories": ["food"],
        "insights": ["trend_warning", "budget_risk"],
    },
    "tip_food_sub_01": {
        "text": "You have an active food delivery subscription. "
                "Verify it's being used enough to justify the cost.",
        "categories": ["food"],
        "insights": ["subscription"],
    },
    # ── Shopping ──────────────────────────────────────────────────────────────
    "tip_shop_spike_01": {
        "text": "Consider a 24-hour cooling-off rule before purchases over ₹2,000.",
        "categories": ["shopping"],
        "insights": ["spending_spike"],
    },
    "tip_shop_spike_02": {
        "text": "Check if this item is available at a lower price on "
                "a competing platform before completing the purchase.",
        "categories": ["shopping"],
        "insights": ["spending_spike"],
    },
    "tip_shop_trend_01": {
        "text": "Your shopping spend is trending upward this month. "
                "Set a weekly discretionary cap to stay on track.",
        "categories": ["shopping"],
        "insights": ["trend_warning", "budget_risk"],
    },
    "tip_shop_sub_01": {
        "text": "Recurring shopping charge detected. Verify this isn't "
                "an unwanted auto-renewal or subscribe-and-save order.",
        "categories": ["shopping"],
        "insights": ["subscription"],
    },
    # ── Transport ─────────────────────────────────────────────────────────────
    "tip_transport_spike_01": {
        "text": "This ride/travel expense is unusually high. Consider "
                "carpooling, public transit, or booking in advance for discounts.",
        "categories": ["transport"],
        "insights": ["spending_spike"],
    },
    "tip_transport_trend_01": {
        "text": "Your transport costs are climbing. Consider a monthly "
                "pass or switching to two-wheelers for short commutes.",
        "categories": ["transport"],
        "insights": ["trend_warning", "budget_risk"],
    },
    "tip_transport_sub_01": {
        "text": "Recurring fuel/transport charges detected. Track your "
                "mileage to check if route optimisation could cut costs.",
        "categories": ["transport"],
        "insights": ["subscription"],
    },
    # ── Utilities ─────────────────────────────────────────────────────────────
    "tip_util_spike_01": {
        "text": "Utility bill spike detected. Check for unusual usage "
                "or billing errors before the next cycle.",
        "categories": ["utilities"],
        "insights": ["spending_spike"],
    },
    "tip_util_trend_01": {
        "text": "Utility bills trending upward. Check for energy leaks, "
                "standby appliances, or seasonal AC usage.",
        "categories": ["utilities"],
        "insights": ["trend_warning", "budget_risk"],
    },
    "tip_util_sub_01": {
        "text": "Recurring utility bill identified. Consider switching "
                "to budget billing for predictable monthly charges.",
        "categories": ["utilities"],
        "insights": ["subscription"],
    },
    # ── Entertainment ─────────────────────────────────────────────────────────
    "tip_ent_spike_01": {
        "text": "Unusual entertainment expense. Check if this was an "
                "accidental in-app purchase or auto-renewal.",
        "categories": ["entertainment"],
        "insights": ["spending_spike"],
    },
    "tip_ent_trend_01": {
        "text": "Entertainment spending is rising. Audit your active "
                "subscriptions — unused ones drain ₹500–1,000/month silently.",
        "categories": ["entertainment"],
        "insights": ["trend_warning", "budget_risk"],
    },
    "tip_ent_sub_01": {
        "text": "Active streaming/entertainment subscription detected. "
                "Check if you've used it in the last 30 days.",
        "categories": ["entertainment"],
        "insights": ["subscription"],
    },
    # ── Finance ───────────────────────────────────────────────────────────────
    "tip_fin_spike_01": {
        "text": "Unexpected financial charge detected. Verify this isn't "
                "a penalty, late fee, or missed EMI payment.",
        "categories": ["finance"],
        "insights": ["spending_spike"],
    },
    "tip_fin_trend_01": {
        "text": "Financial outflows are increasing. Review outstanding "
                "loans and consider prepaying high-interest debt first.",
        "categories": ["finance"],
        "insights": ["trend_warning", "budget_risk"],
    },
    "tip_fin_sub_01": {
        "text": "Recurring EMI/insurance premium identified. Ensure "
                "auto-debit is linked to a funded account to avoid bounce charges.",
        "categories": ["finance"],
        "insights": ["subscription"],
    },
    # ── Health ────────────────────────────────────────────────────────────────
    "tip_health_spike_01": {
        "text": "Significant health expense detected. Check if this is "
                "claimable under your health insurance policy.",
        "categories": ["health"],
        "insights": ["spending_spike"],
    },
    "tip_health_trend_01": {
        "text": "Health-related spending is trending up. Consider "
                "preventive health check-ups to catch issues early.",
        "categories": ["health"],
        "insights": ["trend_warning", "budget_risk"],
    },
    "tip_health_sub_01": {
        "text": "Recurring pharmacy/health charge detected. Ask your "
                "doctor about generic alternatives for regular medications.",
        "categories": ["health"],
        "insights": ["subscription"],
    },
    # ── ATM ───────────────────────────────────────────────────────────────────
    "tip_atm_spike_01": {
        "text": "Large cash withdrawal detected. ATM withdrawals are "
                "harder to track — consider using UPI for spending visibility.",
        "categories": ["atm"],
        "insights": ["spending_spike"],
    },
    "tip_atm_trend_01": {
        "text": "Cash withdrawals are increasing. Untracked cash spending "
                "is the #1 budget leak — try going cashless for a week.",
        "categories": ["atm"],
        "insights": ["trend_warning", "budget_risk"],
    },
    # ── Transfer ──────────────────────────────────────────────────────────────
    "tip_transfer_spike_01": {
        "text": "Unusually large transfer detected. Verify the recipient "
                "and ensure this wasn't an error or unauthorised transaction.",
        "categories": ["transfer"],
        "insights": ["spending_spike"],
    },
    "tip_transfer_trend_01": {
        "text": "Outgoing transfers trending up. Review if recurring "
                "transfers can be reduced or consolidated.",
        "categories": ["transfer"],
        "insights": ["trend_warning", "budget_risk"],
    },
    # ── Generic (category-agnostic) ───────────────────────────────────────────
    "tip_generic_spike_01": {
        "text": "This transaction is significantly above your normal "
                "spending pattern. Review to ensure it was intentional.",
        "categories": [],
        "insights": ["spending_spike"],
    },
    "tip_generic_trend_01": {
        "text": "Spending in this category is trending upward. Consider "
                "setting a monthly category budget to stay on track.",
        "categories": [],
        "insights": ["trend_warning"],
    },
    "tip_generic_budget_01": {
        "text": "Your cumulative spending this month is outpacing your "
                "historical average. Review non-essential expenses.",
        "categories": [],
        "insights": ["budget_risk"],
    },
    "tip_generic_sub_01": {
        "text": "Recurring charge identified. Periodically review all "
                "subscriptions to cancel unused services.",
        "categories": [],
        "insights": ["subscription"],
    },
}
  ```

  Instruction: Replace the exact literal code block above. If the exact Before block is not found exactly once, STOP. Do not infer the edit location.
  Migrate the existing TIP_CORPUS in place.
  Do not replace the full corpus with the sample entries.
  For every existing tip_id, preserve the existing text and convert each value to the new schema:

  {
  "text": existing_text,
  "categories": tuple(existing_categories),
  "insights": tuple(existing_insights),
  }

  Rules:
  - Preserve every existing tip_id unless explicitly deprecated elsewhere.
  - Preserve every existing tip text.
  - Preserve every existing category and insight mapping.
  - Generic wildcard tips may use empty categories/insights only if tip_id starts with "generic_".
  - Non-generic tips must have non-empty categories and insights.
  - Do not introduce "any" wildcard for non-generic tips.
  - If any existing tip cannot be migrated mechanically, STOP and report the exact tip_id.

  For SPECIFIC_MERCHANT_ALIASES:
  Preserve the entire existing alias map.
  Only add or normalize these required entries if missing:

  "amazon": "amazon"
  "amzn": "amazon"
  "amazon prime": "amazon"
  "flipkart": "flipkart"
  "meesho": "meesho"
  "snapdeal": "snapdeal"

  Do not delete existing aliases.

  After:
  A patch-only instruction that explicitly preserves all existing entries and adds only the required entries, migrating the format as stated in the instruction.

  Rollback: Restore original `TIP_CORPUS` and `SPECIFIC_MERCHANT_ALIASES`.

POST-EXECUTION VALIDATION
[ ] `schema.py` contains `INFERRED_SUBCATEGORY` and `SUBCATEGORY_CONFIDENCE`.
[ ] `config.py` uses the new `TIP_CORPUS` structure.
[ ] Linter passes.

[ ] python3 -m py_compile schema.py config.py succeeds.
[ ] python3 -c "from schema import Col; from config import TIP_CORPUS, SPECIFIC_MERCHANT_ALIASES; assert Col.INFERRED_SUBCATEGORY == 'inferred_subcategory'; assert Col.SUBCATEGORY_CONFIDENCE == 'subcategory_confidence'; assert isinstance(TIP_CORPUS, dict); assert isinstance(SPECIFIC_MERCHANT_ALIASES, dict)"
[ ] python3 -c "from config import TIP_CORPUS; assert len(TIP_CORPUS) >= 5; assert all({'text','categories','insights'} <= set(v) for v in TIP_CORPUS.values())"
[ ] python3 -c "from config import SPECIFIC_MERCHANT_ALIASES; required={'amazon','amzn','amazon prime','flipkart','meesho','snapdeal'}; assert required <= set(SPECIFIC_MERCHANT_ALIASES)"
[ ] python3 -c "from config import SPECIFIC_MERCHANT_ALIASES; assert len(SPECIFIC_MERCHANT_ALIASES) >= 20"

GO / NO-GO
All checks pass → proceed to CHECKPOINT [02]
