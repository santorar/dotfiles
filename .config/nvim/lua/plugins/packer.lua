return require('packer').startup(function()
	-- Packer can manage ifself
	use 'wbthomason/packer.nvim'

	-- Colorsheme
    use 'gruvbox-community/gruvbox'
    
    -- TreeSiter
    use {'nvim-treesitter/nvim-treesitter', run = ':TSUpdate'}

    -- lsp config
    use 'neovim/nvim-lspconfig'
	
	-- Nvim-tree
	use {
  		'kyazdani42/nvim-tree.lua',
  		requires = {
    			'kyazdani42/nvim-web-devicons', -- optional, for file icons
  		},
	}
end)
