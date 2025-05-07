
from redis_json_dict import RedisJSONDict
from redis_json_dict.redis_json_dict import ObservableMapping
from redis import Redis


def get_redis_config():
    """Get a fresh Redis connection and config. Enforces RedisJSONDict types."""
    config = RedisJSONDict(Redis("info.smi.nsls2.bnl.gov", db=1), prefix="")
    
    # Initialize empty dicts if they don't exist
    if 'samples' not in config:
        config['samples'] = {}
    if 'operations' not in config:
        config['operations'] = {}
    if 'holders' not in config:
        config['holders'] = {
            "Standard": {
                "type": "standard",
                "garage_bay": "1,1",
                "samples": []
                # a holder['sample'] should have 'id' as the key
            }
        }

def get_stores():
    """Get fresh references to Redis stores"""
    config = get_redis_config()
    samples = config['samples']
    operations = config['operations']
    holders = config['holders']
    
    # Verify all stores are ObservableMapping instances
    if not isinstance(samples, ObservableMapping):
        raise TypeError("samples must be an ObservableMapping")
    if not isinstance(operations, ObservableMapping):
        raise TypeError("operations must be an ObservableMapping")
    if not isinstance(holders, ObservableMapping):
        raise TypeError("holders must be an ObservableMapping")
        
    return samples, operations, holders, config

samps, ops, holders, config = get_stores()