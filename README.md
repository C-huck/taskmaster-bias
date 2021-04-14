# Implicit bias in the adjudication of contestants on a British gameshow (Taskmaster)

## Background

### Precis
- British panel show
- 5 comedians compete to complete meaningless tasks
- Task performance is adjudicated by Greg Davies
- Points are assigned per task (1 - 5 points); there are per-episode and overall winners
- Sample task:
"Catapult this shoe into the bath using a homemade contraption. You may only use your foot to operate the contraption. You may not move the bath or the red mat, and you must build your contraption on the red mat."

### Cast composition, win rate

| 5 contestants per series |  |
|-|-|
| 2 - 3 | White men, of which 1 is 'older' |
| 1 - 2 | White women, of which 1 is 'older' |
| 1 | Non-white person, where 'non-white' is in {black, Indian, Jewish, Samoan} |

| Totals over all series |  |
|-|-|
| 18 | White men |
| 10 | White women |
| 7 | Non-white contestants, of which 1 is a woman |

Expected POC series win rate: 20% (1 in 5 per series)
Observed POC win rate: 0%

## Hypotheses, model

H<sub>0</sub>: No difference in win rate, points-per-episode, or overall rank between white and non-white contestants
H<sub>1</sub>: POCs are adjudicated worse across the board than their non-POC peers, irrespective of gender

Used an OLS with the following formula to predict points per episode based on POC/non-POC and perceived gender. 

```Python 
"Points_per_ep ~ POC + Sex_text"
```

## Results

![Points per episode, sorted by white/non-white](https://github.com/C-huck/taskmaster-bias/blob/main/points_per_epi_s10.png)

