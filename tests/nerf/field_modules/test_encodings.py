"""
Encoding Tests
"""
import pytest
import torch
from mattport.nerf.field_modules import encoding


def test_scaling_and_offset():
    """Test scaling and offset encoder"""
    in_dim = 4
    in_tensor = torch.ones((2, 3, in_dim))

    scaling = 2.0
    offset = 4.5
    encoder = encoding.ScalingAndOffset(in_dim=in_dim, scaling=scaling, offset=offset)

    assert encoder.get_out_dim() == in_dim
    encoded = encoder.encode(in_tensor)
    assert encoded.shape[-1] == in_dim
    assert in_tensor * 6.5 == pytest.approx(encoded)

    with pytest.raises(ValueError):
        encoding.ScalingAndOffset(in_dim=-1)


def test_nerf_encoder():
    """Test NeRF encoder"""
    in_dim = 4
    out_dim = 24
    in_tensor = torch.ones((2, 3, in_dim))

    num_frequencies = 3
    min_freq_exp = 0
    max_freq_exp = 3
    encoder = encoding.NeRFEncoding(
        in_dim=in_dim, num_frequencies=num_frequencies, min_freq_exp=min_freq_exp, max_freq_exp=max_freq_exp
    )
    assert encoder.get_out_dim() == out_dim

    in_tensor = torch.ones((2, 3, in_dim))
    encoded = encoder.encode(in_tensor)
    assert encoded.shape[-1] == out_dim
    assert torch.max(encoded) == 1

    in_tensor = torch.zeros((2, 3, in_dim))
    encoded = encoder.encode(in_tensor)
    assert encoded.shape[-1] == out_dim
    assert torch.min(encoded) == 0


def test_rff_encoder():
    """Test RFF encoder"""
    in_dim = 3
    out_dim = 24
    in_tensor = torch.ones((2, 3, in_dim))

    num_frequencies = 12
    scale = 5
    encoder = encoding.RFFEncoding(in_dim=in_dim, num_frequencies=num_frequencies, scale=scale)
    assert encoder.get_out_dim() == out_dim

    in_tensor = torch.ones((2, 3, in_dim))
    encoded = encoder.encode(in_tensor)
    assert encoded.shape[-1] == out_dim