from scipy.stats import false_discovery_control, hmean, permutation_test
from .stats import get_corrected_hmpval, mean_diff

def get_p_vals(data, num_perm=10000):
    '''Mostly a wrapper for scipy.stats.permutation_test
    
    Parameters
    ------------
    data: array containing samples from two different power spectra

    num_perm: number of permutations to run in the permutation_test
    '''
    



def p_correction(p_vals):
    corrected_p_vals = {}
    corrected_p_vals['Bonfereoni'] = p_vals / len(p_vals)
    corrected_p_vals['BH'] = false_discovery_control(p_vals, axis=0, method='bh')
    corrected_p_vals['HMP'] = get_corrected_hmpval(hmean(p_vals), len(p_vals))
    